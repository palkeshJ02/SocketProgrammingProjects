import socket
client = socket.socket()
client.connect(('localhost',12345))


## Now we wiill add function to encrypt and decrypt using a key. 
## User must know key to succesfully decrypt messages. 
def encrypt(message, key):
	message = message.encode()
	key = key.encode()
	result = bytearray()
	for i in range(len(message)):
		result.append(message[i] ^ key[i%len(key)])
	return bytes(result)
	
key = input("Enter your key: ")
print("You can end coversation by typing end")
while True: 

	message = input("You : ")
	message = encrypt(message, key)
	client.send(message)
	if message == "end":
		print("Ending Coversation...........")
		break
	response = client.recv(1024)
	response = encrypt(response.decode(), key).decode(errors='replace')
	if response == "end" or not response: 
		print("Ending Coversation...........")
		break
	print("Opponent : ", response)

client.close()


