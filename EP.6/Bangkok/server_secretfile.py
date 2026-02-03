import socket
############CIPHER###############
from cryptography.fernet import Fernet

with open('secret.key','rb') as f:
    key = f.read()

cipher = Fernet(key)
#################################

files_list = ['hellopython.pdf','test.pdf']

#################################
serverip = '192.168.100.234'
port = 8500

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

server.bind((serverip,port))
server.listen(5)
print('waiting...')

client, addr = server.accept()
print('connected from...',addr)

data = client.recv(1024) # encrypted_data
print('Data (encrypted): ',data)
filename_decrypted = cipher.decrypt(data).decode(encoding='utf-8')
print('Data from client(decrypted): ',filename_decrypted)

if filename_decrypted not in files_list:
    # NO FILE IN THE LIST
    response = 'File not found'
    encrypted_response = cipher.encrypt(response.encode(encoding='utf-8'))
    client.send(encrypted_response)
    client.close()
    server.close()
    exit()

print('Found...')

with open(filename_decrypted, 'rb') as f:
    encrypted_data = cipher.encrypt(f.read())

client.sendall(encrypted_data)
client.close()
server.close()