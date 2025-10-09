from flask import Flask
import random
import time

app = Flask(__name__)

@app.route('/')
def hello():
    # ---- Simulate random latency (response time > 1s about 25% of time) ----
    if random.random() < 0.25:
        delay = random.uniform(1.2, 2.5)  # delay between 1.2s and 2.5s
        time.sleep(delay)

    # ---- Simulate 5xx errors (20% of requests) ----
    if random.random() < 0.2:
        return "Internal Server Error (Test)", 500

    # ---- Normal successful response ----
    return "Hello, World from Cloud Run! deployed using GitHub Actions", 200


if __name__ == '__main__':
    # Run on Cloud Run's expected port
    app.run(host='0.0.0.0', port=8080)
