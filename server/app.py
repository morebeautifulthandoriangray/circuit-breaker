from flask import Flask
import random
import time


app = Flask(__name__)

data = ["apple", "pineapple"]


@app.route('/')
def hello_world():
    return 'HEEEEEYYEYEYEYEY'

@app.route('/fault')
def faulty_endpoint():
    r = random.randint(0, 1)
    if r == 0:
        time.sleep(5)

    return {
        "msg": "I've failed."
    }, 500


@app.route('/randfail')
def fail_randomly_endpoint():
    r = random.randint(0, 1)
    if r == 0:
        return data, 200

    return {
        "msg": "I will fail (sometimes)."
    }, 500


if __name__ == '__main__':
    app.run()
