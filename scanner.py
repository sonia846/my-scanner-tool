import socket
import sys

# Target server (Nmap ki official testing site)
target = "scanme.nmap.org" 

print("-" * 50)
print(f"Scanning Target: {target}")
print("-" * 50)

# Kuch common ports jinhein hum check karenge
ports = [21, 22, 80, 443, 8080]

try:
    for port in ports:
        # TCP connection setup
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0) # 1 second ka timeout
        
        # Connection check karne ka function
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: Closed")
            
        s.close()

except KeyboardInterrupt:
    print("\nExiting script.")
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()

except socket.error:
    print("\nCould not connect to server.")
    sys.exit()

