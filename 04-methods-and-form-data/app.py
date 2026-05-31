from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/welcome/<name>")
def welcome(name):
    return f"Welcome {name}!"


@app.route("/login", methods=["POST", "GET"])
def login():
    # POST reads submitted form data, GET reads query-string data.
    if request.method == "POST":
        user = request.form.get("nm")
    else:
        user = request.args.get("nm")

    if not user:
        return render_template("login.html")

    return redirect(url_for("welcome", name=user))


if __name__ == "__main__":
    app.run(debug=True)