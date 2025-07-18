# main.py
import os
from services.link_client import LinkClient
from flask import Flask, jsonify
import datetime
import sys

app = Flask(__name__)

def check_environment():
    """Check and validate required environment variables"""
    missing_vars = []
    
    # When running as web service, check for PORT
    if any(arg.startswith('--port=') for arg in sys.argv):
        if not os.getenv('PORT'):
            missing_vars.append('PORT')
    
    # Always check for LINK_KEY
    if not os.getenv('link_key'):
        missing_vars.append('LINK_KEY')
    
    if missing_vars:
        print("\nError: Missing required environment variables:")
        print("Please set the following variables:")
        
        if 'PORT' in missing_vars:
            print("\nFor web service:")
            print("export PORT=8080")
        
        if 'LINK_KEY' in missing_vars:
            print("\nFor Link API:")
            print('export link_key="your-api-key-here"')
            
        print("\nFor convenience, you can set both at once:")
        print('export PORT=8080 link_key="your-api-key-here"')
        print("\nOr for production deployment, set these in your DigitalOcean app configuration.\n")
        return False
    return True

def test_link_connection():
    """Test the Link gRPC connection and return the results"""
    results = {
        'timestamp': datetime.datetime.now().isoformat(),
        'status': 'unknown',
        'message': ''
    }
    
    try:
        if not os.getenv("link_key"):
            results.update({
                'status': 'error',
                'message': 'LINK_KEY environment variable is not set'
            })
            return results

        print("Attempting to connect to Link service...")
        with LinkClient() as client:
            results.update({
                'status': 'success',
                'message': 'Successfully connected to Link gRPC service'
            })
            
    except Exception as e:
        results.update({
            'status': 'error',
            'message': f'Error occurred: {str(e)}'
        })
    
    return results

@app.route('/')
def home():
    """Web endpoint that returns Hello World and timestamp"""
    timestamp = datetime.datetime.now().isoformat()
    return jsonify({
        'message': 'Hello World',
        'timestamp': timestamp,
        'environment': {
            'port': os.getenv('PORT', 'not set'),
            'link_key_set': 'yes' if os.getenv('link_key') else 'no'
        }
    })

@app.route('/link/test')
def test_link():
    """Web endpoint that tests the Link gRPC connection"""
    results = test_link_connection()
    return jsonify(results)

def main():
    """Run the gRPC connection test directly"""
    if not check_environment():
        sys.exit(1)
        
    results = test_link_connection()
    print(f"\nStatus: {results['status']}")
    print(f"Message: {results['message']}\n")

if __name__ == "__main__":
    # If PORT environment variable is set, run as web service
    if os.getenv('PORT'):
        if not check_environment():
            sys.exit(1)
        port = int(os.getenv('PORT'))
        app.run(host='0.0.0.0', port=port)
    else:
        # Otherwise run the gRPC test directly
        main()