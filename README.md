# Nice Space Server

A Python application that demonstrates gRPC communication with Link service and provides a web interface.

## Requirements

- Python 3.x
- Virtual environment (recommended)
- Link API key
- DigitalOcean account for deployment

## Environment Variables

The application requires the following environment variables:

1. `LINK_KEY` - Your Link API key
2. `PORT` - The port number (when running as web service)

### Setting Environment Variables

For local development:
```bash
# Set variables individually
export PORT=8080
export link_key="your-api-key-here"

# Or set both at once
export PORT=8080 link_key="your-api-key-here"
```

For DigitalOcean deployment:
- Set these in your app's environment variables configuration
- The `PORT` variable will be set automatically by the platform

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/nice-space-server.git
cd nice-space-server
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Unix/macOS
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:

As a command-line tool (tests gRPC connection):
```bash
export link_key="your-api-key-here"
python3 main.py
```

As a web service:
```bash
export PORT=8080 link_key="your-api-key-here"
python3 main.py
```

## Web Endpoints

- `/` - Returns Hello World with timestamp and environment status
- `/link/test` - Tests the Link gRPC connection

## Deployment on DigitalOcean

1. Push your code to GitHub
2. Create a new app in DigitalOcean App Platform
3. Connect to your repository
4. Set the required environment variables:
   - `LINK_KEY`: Your Link API key
   - `PORT`: Will be set automatically
5. Deploy the application

The application will use the Procfile configuration to run with gunicorn in production. 