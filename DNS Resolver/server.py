import socket 

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 12345))
print(f"Server listening for Queries......(To Stop server use Ctrl+C)")

while True: 
    domain , addr  = server.recvfrom(1024)
    domain = domain.decode()
    print("Query to resolve : ", domain )

    try : 
        ip = socket.gethostbyname(domain)
        print(f"{domain}:{ip}")

    except socket.gaierror:
        ip = "Not Resolved"
    
    server.sendto(ip.encode(), addr)
