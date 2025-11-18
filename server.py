import socket


serverip = '192.168.1.100'
port = 8500

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

server.bind((serverip,port))
server.listen(5)
print('waiting...')

client, addr = server.accept()
print('connected from...',addr)

data = client.recv(1024).decode('utf-8')
print('Data: ',data)

client.send('we got your message!'.encode('utf-8'))
client.close()