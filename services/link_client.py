# services/link_client.py
import grpc
import os
from typing import Optional
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import only what we need
from google.protobuf import empty_pb2

class LinkClient:
    def __init__(self, host: str = 'linkone-three.pilot.seamless.lastlock.com', 
                 port: str = "443",
                 api_key: Optional[str] = None):
        self.host = host
        self.port = port
        self.api_key = api_key or os.getenv("link_key")
        
        if not self.api_key:
            raise ValueError("API key must be provided either through constructor or LINK_KEY environment variable")
        
        # Create secure channel with credentials
        self.channel = grpc.secure_channel(
            f"{self.host}:{self.port}",
            grpc.composite_channel_credentials(
                grpc.ssl_channel_credentials(),
                grpc.access_token_call_credentials(self.api_key)
            )
        )
        
        # Test connection with a timeout
        try:
            grpc.channel_ready_future(self.channel).result(timeout=5)
            print("Successfully connected to gRPC server")
        except grpc.FutureTimeoutError:
            print("Failed to connect: timeout waiting for channel to be ready")
            raise
        except grpc.RpcError as e:
            print(f"Failed to connect: {e.code()} - {e.details()}")
            raise

    def close(self):
        """Close the gRPC channel"""
        self.channel.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()