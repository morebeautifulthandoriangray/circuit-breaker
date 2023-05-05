from flask import Flask
import random
import time

app = Flask(__name__)

data = ["apple", "pineapple"]


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/data')
def data_data():
    return data, 200


@app.route('/fail')
def faulty_endpoint():
    r = random.randint(0, 1)
    if r == 0:
        time.sleep(5)

    return {
        "msg": "I will fail."
    }, 500


@app.route('/randfail')
def fail_randomly_endpoint():
    r = random.randint(0, 1)
    if r == 0:
        return {
            "msg": "Success msg"
        }, 200

    return {
        "msg": "I will fail (sometimes)."
    }, 500


if __name__ == '__main__':

    app.run(port=5000)
