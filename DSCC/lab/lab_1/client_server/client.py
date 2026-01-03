import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = input("Enter Server IP Address: ")  # Example: 192.168.1.5
server_port = 5000
client_socket.connect((server_ip, server_port))
print("Connected to Server.\nType 'exit' to quit.")

while True:
    message = input("Client: ")
    client_socket.send(message.encode())
    if message.lower() == "exit":
        break
    data = client_socket.recv(1024).decode()
    print("Server:", data)

client_socket.close()

