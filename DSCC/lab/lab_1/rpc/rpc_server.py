from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime

def calculate_age(dob_str):
    dob = datetime.strptime(dob_str, "%d-%m-%Y")
    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

server = SimpleXMLRPCServer(("0.0.0.0", 9000))
print("RPC Server running on port 9000...")
server.register_function(calculate_age, "calculate_age")
server.serve_forever()

