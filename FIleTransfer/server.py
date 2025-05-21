import socket 
server = socket.socket()
server.bind(('localhost', 12345))

## A list of Usernames and passwords
authorized_users = {
                    "John":"cat123",
                    "Jack":"oggy23",
                    "Bob":"doggo11"

}

server.listen()

client, addr = server.accept()

print("File Transfer Request From ", addr)
data  = client.recv(1024).decode()
username, password = data.split(":")
print("Authorizing user .........")
if username in authorized_users.keys():
    if authorized_users[username]==password:
        print("Authorization Successful")
        code = str(1)
        client.send(code.encode())

        with open("testfile1.txt", "r") as f:
            data = f.read()
            client.send(data.encode())
        print("File Tarnsfer Successful!")
        
    else:
        print("Authorization failure")
        code = str(2)
        client.send(code.encode())

else:
    print("Authorization failure")
    code = str(3)
    client.send(code.encode())


message = "Closing Connection ........."
print(message)


client.close()

server.close()
