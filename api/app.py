# create a flask app, import all the relevant modules and create the app
from flask import Flask


# create an instance of the flask app
app = Flask(__name__)


# create a route decorator
@app.route("/")
def index():
    return "hello world"


# create a route decorator
@app.route("/tuna")
def tuna():
    return "<h2> tuna is good </h2>"


# initiate the app
if __name__ == "__main__":
    app.run(debug=True, port=80)
