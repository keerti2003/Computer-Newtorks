import socket

# DNS server configuration
dns_server_address = "localhost"
dns_server_port = 53

# Hostname to query
hostname = input("Enter domain name to search for: ")
# Create a UDP socket for DNS communication
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send the DNS query to the server
client_socket.sendto(hostname.encode(), (dns_server_address, dns_server_port))

# Receive and print the response from the server
response, server_address = client_socket.recvfrom(1024)
print(f"IP address for {hostname}: {response.decode()}")

# Close the socket
client_socket.close()
