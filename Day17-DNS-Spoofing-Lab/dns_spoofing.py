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
