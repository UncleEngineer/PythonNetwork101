import socket
############CIPHER###############
from cryptography.fernet import Fernet

with open('secret.key','rb') as f:
    key = f.read()

cipher = Fernet(key)
#################################
############FROM SERVER##############
serverip = '192.168.100.234'
port = 8500

while True:
    request_file = input('Enter message: ')

    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    server.connect((serverip,port))
    # encrypt data
    encrypted_msg = cipher.encrypt(request_file.encode(encoding='utf-8'))
    server.send(encrypted_msg)

    encrypted_data = b""
    while True:
        data = server.recv(4096)
        print('DATA: ')
        if not data:
            break
        encrypted_data += data

    
    data_decrypted = cipher.decrypt(encrypted_data)

    with open('received_'+ request_file, 'wb') as f:
        f.write(data_decrypted)

    print('You got the file: ', 'received_'+ request_file)
    server.close()