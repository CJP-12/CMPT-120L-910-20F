from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to my project! Add a /hidden/ to the end of the URL to see another page!<h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/hidden/")
def admin():
    return redirect(url_for("user", name= "<h1>Secret Page! Add a /wacky/ to the end of the URL to see another page!<h1>"))

@app.route("/wacky/")
def player():
    return redirect(url_for("user", name="<h1>Wacky Road! Add a /tired/ to the end of the URL to see another page!<h1>"))

if __name__ == "__main__":
    app.run()
