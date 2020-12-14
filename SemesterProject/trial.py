from flask import Flask, redirect, url_for, render_template

from flask.html import 
app = Flask(__name__)

@app.route("/")
def home():
    return render_template(flask.html)


@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/hidden/")
def admin():
    return redirect(url_for("user", name= "<h1>Secret Page!<h1>"))

if __name__ == "__main__":
    app.run()
