import socket

def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0: pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0' * pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    checkword = tmp
    return checkword

def decodeData(data, key):
    l_key = len(key)
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)
    return remainder



server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_host = '127.0.0.1'
server_port = 12345
server_socket.bind((server_host, server_port))
print("UDP server is up and listening...")

key = "1001"

while True:
    data, client_address = server_socket.recvfrom(1024)
    print("Received data from", client_address)

    decoded_data = data.decode('utf-8')
    
    ans = decodeData(decoded_data, key)

    temp = "0" *(len(key)-1)
    if ans == temp:
        ack_message = "ACK: Data received successfully"
    else:
        ack_message = "NACK: Data received with errors"

    server_socket.sendto(ack_message.encode('utf-8'), client_address)
