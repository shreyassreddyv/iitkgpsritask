import socket
import threading
port = 5052
host = "0.0.0.0"
ADDRESS = (host,port)
Format = 'utf-8'
header = 64
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDRESS)
clients = []
usernames = []
def broadcast(message):
    for client in clients:
        client.send(message.encode(Format))
def cater(client,username):
    while True:
        message = client.recv(5000)
        message = message.decode(Format)
        if message == "/quit":
            break
        elif message == "/list":
            client.send(f"[SERVER RESPONSE]:\n".encode(Format))
            for username in usernames:
                client.send((username+"\n").encode(Format))
        else:
            broadcast(f"[{username}]:{message}")
    index = clients.index(client)
    clients.remove(client)
    ind = usernames.index(username)
    usernames.remove(username)
    client.close()
def pstart():
    server.listen()
    print(f"The [SERVER] is listening on {host}\n")
    while True:
        client, address = server.accept()
        clients.append(client)
        client.send("user".encode(Format))
        username = client.recv(1024).decode(Format)
        usernames.append(username)
        client.send("Welcome to ChatNet (/quit to quit)\n".encode(Format))
        print
        broadcast(f"{username} joined the chat!\n")            
        cater_thread = threading.Thread(target=cater,args=(client,username))
        cater_thread.start()

pstart()
    
