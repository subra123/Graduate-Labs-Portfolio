import xmlrpc.client

server_ip = input("Enter RPC Server IP: ")
proxy = xmlrpc.client.ServerProxy(f"http://{server_ip}:9000/")

dob = input("Enter your Date of Birth (dd-mm-yyyy): ")
age = proxy.calculate_age(dob)
print(f"Your Age is: {age}")

