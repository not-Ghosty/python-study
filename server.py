from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Hello world"


if __name__ == "server":
    print("Server file imported")

if __name__ == "__main__":
    print("Server started")
    app.run(debug=True)
