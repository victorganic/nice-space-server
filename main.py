import datetime
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{timestamp}] Hello World"

if __name__ == "__main__":
    # Get port from environment variable or default to 8080
    port = int(os.environ.get("PORT", 8080))
    # Run the Flask app
    app.run(host='0.0.0.0', port=port) 