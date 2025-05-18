import socket

server = socket.socket()
server.bind(('localhost', 12345))
server.listen()
client, addr = server.accept() 
print("Connection request from: " + str(addr))

while True:
    data = client.recv(1024).decode()
    if not data:
        break
    print("Message : ", str(data))
    data = input("Your message: ")
    client.send(data.encode())

client.close()

