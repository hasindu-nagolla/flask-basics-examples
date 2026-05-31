from flask import Flask, redirect, request, url_for

app = Flask(__name__)


@app.route("/welcome/<name>")
def welcome(name):
    return f"Welcome {name}!"


@app.route("/login", methods=["POST", "GET"])
def login():
    # POST reads submitted form data, GET reads query-string data.
    if request.method == "POST":
        user = request.form["nm"]
    else:
        user = request.args.get("nm")

    return redirect(url_for("welcome", name=user))


if __name__ == "__main__":
    app.run(debug=True)