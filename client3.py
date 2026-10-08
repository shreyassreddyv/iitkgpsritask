import socket
import threading
port = 5052
host = "127.0.0.1"
ADDRESS = (host,port)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
header = 64
Format = 'utf-8'
client.connect(ADDRESS)
username = input("Enter your username :")
def recieve():
    while True:
        try:
            message = client.recv(5000).decode(Format)
        except OSError:
            break
        if not message:
            break
        if message == "user":
            client.send(username.encode(Format))
        else:
            print(message)
def send(message):
    client.send(message.encode(Format))

thread_recieve = threading.Thread(target = recieve)
thread_recieve.start()
message = input("")
while message != "/quit":
    send(message)
    message = input("")

send("/quit")
client.close()

    
    
    
