import socket
obj = socket.socket()
obj.connect(('localhost',12345))
message = input("Your Message (Enter q to end chat): ")
while message != 'q':
   obj.send(message.encode())
   data = obj.recv(1024).decode()
   print ('Received from server: ' + data)
   message = input("Your Message (Enter q to end chat): ")
obj.close()


