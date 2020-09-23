from flask import Flask
import requests
import time

app = Flask(__name__)


@app.route('/')
def home():
    return 'Server running'


@app.route('/wakeAffari')
def wake_affari():
    # inner()

    return 'Hello, World!'


def inner():
    resp = requests.get('https://affari.herokuapp.com/').content
    return(resp)


while True:
    print(inner())
    time.sleep(10)


if __name__ == "__main__":
    app.run(port=5100)
