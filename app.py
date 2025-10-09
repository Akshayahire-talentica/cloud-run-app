from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello():
    # Simulate 20% of requests returning HTTP 500
    if random.random() < 0.2:
        return "Internal Server Error (Test)", 500
    return "Hello, World from Cloud Run! deployed using GitHub Actions", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
