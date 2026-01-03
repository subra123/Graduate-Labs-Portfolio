import socket

# Create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = "0.0.0.0"     # Listen on all interfaces
server_port = 5000
server_socket.bind((server_ip, server_port))
server_socket.listen(1)
print(f"Server listening on {server_ip}:{server_port}")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print("Client:", data)
    message = input("Server: ")
    conn.send(message.encode())
    if message.lower() == "exit":
        break

conn.close()
server_socket.close()

