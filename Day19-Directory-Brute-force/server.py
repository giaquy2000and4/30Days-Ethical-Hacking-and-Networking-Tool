from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Home Page"

@app.route("/admin")
def admin():
    return "Admin Page"

@app.route("/dashboard")
def dashboard():
    return "Dashboard"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
