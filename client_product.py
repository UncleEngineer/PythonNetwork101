import socket

############FROM SERVER##############
serverip = '10.25.12.131'
port = 8500

while True:
    data = input('Enter message: ')

    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    server.connect((serverip,port))
    server.send(data.encode('utf-8'))

    data_server = server.recv(1024).decode('utf-8')
    print('Data from server: ',data_server)
    server.close()