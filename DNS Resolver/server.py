import socket 
from collections import OrderedDict

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 12345))
print(f"Server listening for Queries......(To Stop server use Ctrl+C)")

cache = OrderedDict()
while True: 
    domain , addr  = server.recvfrom(1024)
    domain = domain.decode()
    print("Query to resolve : ", domain )

    try : 
        if domain in cache.keys():
            ip = cache[domain]
            print("Using cache...")
        else:
            ip = socket.gethostbyname(domain)
            cache[domain]= ip
            if len(cache.keys()) > 10 :
                cache.popitem(last=False)
                print("Cache Limit Exceeded! Removing Oldest Entry...")

        print(f"{domain}:{ip}")
        

    except socket.gaierror:
        ip = "Not Resolved"
    
    server.sendto(ip.encode(), addr)
