import csv
import socket


def read_dns_database(filename):
    dns_database = {}
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            hostname, ip_address = row
            dns_database[hostname] = ip_address
    return dns_database


dns_database_filename = "dns_database.csv"
dns_port = 53

dns_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dns_socket.bind(("localhost", dns_port))

# Read the DNS database from the CSV file
dns_database = read_dns_database(dns_database_filename)

print(f"DNS server is running on port {dns_port}...")

# Start the DNS server loop
while True:
    # Receive a DNS query from a client
    query, client_address = dns_socket.recvfrom(1024)
    hostname = query.decode().strip()

    # Lookup the IP address for the hostname
    ip_address = dns_database.get(hostname, "Hostname not found")

    # Send the IP address back to the client
    dns_socket.sendto(ip_address.encode(), client_address)
