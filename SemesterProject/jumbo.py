from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to my project! http://127.0.0.1.5000/hidden/<h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/hidden/")
def admin():
    return redirect(url_for("user", name= "<h1>Secret Page!<h1>"))

if __name__ == "__main__":
    app.run()
