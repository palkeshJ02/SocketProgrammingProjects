import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True : 
    domain = input("Enter domain to resolve (or 'exit') : ")
    if domain.lower() == 'exit':
        break

    client.sendto(domain.encode(), ('localhost', 12345))
    response, _ = client.recvfrom(1024)
    print(domain," : ", response.decode())


client.close()