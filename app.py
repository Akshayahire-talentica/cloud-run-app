from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World from Cloud Run! deployed using GitHub Actions"

# ⚡️ Latency testing endpoint
# This route intentionally delays the response for testing Cloud Monitoring alerts.
@app.route('/slow')
def slow():
    # Introduce artificial delay (in seconds)
    delay_seconds = 5
    start_time = time.time()

    # Keep CPU busy + sleep for realistic delay
    while time.time() - start_time < delay_seconds:
        _ = [x**2 for x in range(10000)]  # small CPU load

    return f"This /slow endpoint took about {delay_seconds} seconds to respond!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)



