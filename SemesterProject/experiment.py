from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template ("hello.html")

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/hidden/")
def admin():
    return render_template ("about.html")

if __name__ == "__main__":
    app.run()