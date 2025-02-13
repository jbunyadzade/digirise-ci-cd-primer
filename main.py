from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/hello-again")
def hello_again():
    return "Hello again!"


if __name__ == "__main__":
    app.run(debug=True)
