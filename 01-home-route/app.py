from flask import Flask

# __name__ lets Flask find app resources relative to this module.
app = Flask(__name__)


@app.route("/")
def hello():
    """Return a simple response for the home route."""
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)