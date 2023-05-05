import http
import requests

from flask import Flask

app = Flask(__name__)

faulty_endpoint = "http://localhost:5000/fail"
success_endpoint = "http://localhost:5000/data"
random_status_endpoint = "http://localhost:5000/randfail"


@app.route('/status')
def make_request(url):
    try:
        response = requests.get(url, timeout=0.3)
        if response.status_code == http.HTTPStatus.OK:
            print(f"Call to {url} succeed with status code = {response.status_code}")
            return "response"
        if 500 <= response.status_code < 600:
            print(f"Call to {url} failed with status code = {response.status_code}")
            raise Exception("Server Issue")
    except Exception:
        print(f"Call to {url} failed")
        raise


if __name__ == '__main__':
    app.run()

