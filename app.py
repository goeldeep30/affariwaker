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


if __name__ == "__main__":

    def inner():
        resp = requests.get('https://affari.herokuapp.com/').content
        return(resp)

    for count in range(60 * 10):
        print(inner())
        time.sleep(5)

    app.run(port=5100)
