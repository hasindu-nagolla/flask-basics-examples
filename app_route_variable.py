from flask import Flask

app = Flask(__name__)


@app.route("/hello/<name>")
def hello_name(name):
    """Use a dynamic URL segment and greet the provided name."""
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)