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
    data = input('Enter message: ')

    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    server.connect((serverip,port))
    # encrypt data
    encrypted_msg = cipher.encrypt(data.encode(encoding='utf-8'))
    server.send(encrypted_msg)

    data_server = server.recv(1024)
    data_decrypted = cipher.decrypt(data_server)
    print('Data from server(decrypted): ',data_decrypted)
    server.close()