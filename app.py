from flask import Flask, make_response
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    data = {
        "head": {
            "status": "success"
        },
        "body": {

        }
    }
    resp = make_response(data)
    return resp


@app.route('/about')
def about():
    return os.path.join('11', '22')


@app.route("/set_cookies")
def set_cookie():
    resp = make_response("success")
    resp.set_cookie("w3cshool", "w3cshool", max_age=3600, httponly=True)
    return resp


if __name__ == '__main__':
    app.run("0.0.0.0")
