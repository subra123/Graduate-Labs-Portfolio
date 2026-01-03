import socket
import threading
import os

PORT = int(input("Enter port for this peer: "))

# Server: send file list to any peer that connects
def server():
    s = socket.socket()
    s.bind(("0.0.0.0", PORT))
    s.listen(1)
    print(f"Peer server running on port {PORT}...")
    while True:
        conn, addr = s.accept()
        files = os.listdir(".")
        conn.send("\n".join(files).encode())
        conn.close()

# Start server in background thread
threading.Thread(target=server, daemon=True).start()

# Client: connect to another peer and show its files
while True:
    inp = input("Enter peer IP:PORT to connect (or 'exit'): ")
    if inp.lower() == "exit":
        break
    ip, port = inp.split(":")
    c = socket.socket()
    c.connect((ip, int(port)))
    print("Files in peer:", c.recv(4096).decode())
    c.close()

