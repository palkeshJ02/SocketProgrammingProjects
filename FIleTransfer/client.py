import socket

client = socket.socket()

client.connect(('localhost', 12345))
 
username = str(input('Username : '))
password = str(input('Password : '))
message = f"{username}:{password}"
client.send(message.encode())

message = client.recv(1024)
code = message.decode()
if int(code)==1:
    print("Welcome to our platform! File Transfer beginning shortly.....")
    with open("testfile2.txt", "a") as f:
        data = client.recv(1024)
        f.write(data.decode())
    print("Transfer Complete!\nConnection Closing .....")
if int(code)==2:
    print("Incorrect Password! \n Closing Connection .........")
if int(code)==3:
    print("User not registered! \nClosing Connection .........")

client.close()