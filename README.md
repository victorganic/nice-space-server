# Nice Space Server

A simple Python application that prints "Hello World", designed to be deployed on DigitalOcean App Platform.

## Project Overview 

This project demonstrates a basic Python application deployment on DigitalOcean's App Platform. It serves as a minimal example of how to set up and deploy a Python script in a cloud environment.

## Requirements

- Python 3.x
- DigitalOcean account for deployment

## Project Structure

```
nice-space-server/
├── README.md
├── main.py        # Main application file
├── Procfile       # Deployment process file
└── requirements.txt
```

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/nice-space-server.git
cd nice-space-server
```

2. Run the application locally:
```bash
python main.py
```

## Deployment on DigitalOcean

1. Fork or clone this repository to your GitHub account

2. Make sure your repository contains all required files:
   - `main.py` - The Python script
   - `Procfile` - Contains `web: python main.py`
   - `requirements.txt` - Python dependencies (empty for this simple app)

3. Log in to your DigitalOcean account

4. Go to the App Platform section

5. Click "Create App"

6. Select your GitHub repository

7. Configure your app:
   - Choose Python environment
   - Select the branch you want to deploy
   - Important: Leave the "Run Command" field empty (the Procfile will handle this)

8. Click "Deploy"

### Deployment Configuration Notes

The `Procfile` in this repository contains:
```
web: python main.py
```
This tells DigitalOcean App Platform exactly how to run the application. The `web:` prefix is important as it indicates this is a web process.

### Troubleshooting Deployment

If you see this error:
```
ERROR: failed to launch: determine start command: when there is no default process a command is required
```
Check that:
1. The `Procfile` exists in your repository root
2. The `Procfile` content is exactly `web: python main.py`
3. The "Run Command" field in DigitalOcean App Platform is empty

## Contributing

Feel free to submit issues and enhancement requests.

## License

[MIT](https://opensource.org/licenses/MIT) 