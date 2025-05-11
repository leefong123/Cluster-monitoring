from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from flask import Flask, Response, jsonify
import random
import time

app = Flask(__name__)

# Metrics
TOTAL_HTTP_REQUESTS = Counter('http_requests_total', 'Total number of HTTP requests')
TOTAL_HTTP_ERRORS = Counter('http_errors_total', 'Total number of HTTP errors')

@app.route('/')
def home():
    TOTAL_HTTP_REQUESTS.inc()
    return jsonify({"message": "Hello from myFlask app!"})

@app.route('/error')
def error():
    TOTAL_HTTP_REQUESTS.inc()
    TOTAL_HTTP_ERRORS.inc()
    return jsonify({"error": "Something went wrong"}), 500

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':

    random_no = random.randint(2,6)
    if (random_no % 2) > 0:
        print(f'Sleeping... random no: {random_no}')
        time.sleep(3600)
    else:
        print("Creating run.txt")
        with open('/tmp/run.txt', "w") as file:
            file.write("Running... ")


    app.run(host='0.0.0.0', port=8000)

