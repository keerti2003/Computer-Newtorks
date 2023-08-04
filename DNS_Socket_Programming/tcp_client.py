import socket

# DNS server configuration
dns_server_address = "localhost"
dns_server_port = 53

# Hostname to query
hostname = input("Enter domain name to search for: ")

# Create a TCP socket for DNS communication
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the DNS server
client_socket.connect((dns_server_address, dns_server_port))

# Send the DNS query to the server
client_socket.send(hostname.encode())

# Receive and print the response from the server
response = client_socket.recv(1024).decode()
print(f"IP address for {hostname}: {response}")

# Close the socket
client_socket.close()
