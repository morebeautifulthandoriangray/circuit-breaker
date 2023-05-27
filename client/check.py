from flask import Flask, jsonify, request
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

failure_counter = 0
failure_time = None
time_for_recovery = timedelta(seconds=5)

# faulty_endpoint = "http://localhost:5000/fail"
# success_endpoint = "http://localhost:5000/data"
random_status_endpoint = "http://localhost:5000/randfail"


@app.route('/')
def make_first_request():
    return 'HEEEEEEYYYYY'


@app.route('/status')
def make_request(url=random_status_endpoint):
    global failure_counter, failure_time

    if failure_time is not None and datetime.now() - failure_time < time_for_recovery:
        return jsonify({'status': 'Not available'}), 503

    try:
        response = requests.get(url, timeout=0.3)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException:
        failure_counter += 1
        if failure_counter >= 5:
            failure_time = datetime.now()
            return jsonify({'status': 'Not available'}), 503



if __name__ == '__main__':
    app.run()
