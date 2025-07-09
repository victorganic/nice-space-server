import sys
import datetime

def main():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"[{timestamp}] Hello World"
    print(message)
    # Ensure output is flushed immediately
    sys.stdout.flush()

if __name__ == "__main__":
    main() 