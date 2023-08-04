import socket

def xor(a, b):
    result = []
    for i in range(1,len(b)):
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



def encodeData(data, key):
    l_key = len(key)
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_host = '127.0.0.1'
server_port = 12345

input_string = input("Enter data you want to send: ")
data = ''.join(format(ord(x), 'b') for x in input_string)
print("Data to be sent:", data)

key = "1001"
encoded_data = encodeData(data, key)
print("Encoded data:", encoded_data)

client_socket.sendto(encoded_data.encode('utf-8'), (server_host, server_port))

response, server_address = client_socket.recvfrom(1024)
response = response.decode('utf-8')
print("Received acknowledgement from server:", response)

client_socket.close()
