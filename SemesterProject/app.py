from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to my project!<h1>"

@app.route("/<name>")
def user(name):
    return f"Hello! {name}"

@app.route("/hidden/")
def admin():
    return redirect(url_for("user", name= "<h1>Secret Page!<h1>"))

app.route("/about/")
def about():
    return redirect(render_template ("personality.html"))

if __name__ == "__main__":
    app.run()
