import socket

product = {'apple':50,'banana':30,'mango':20}

serverip = '10.25.12.131'
port = 8500

while True:
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    server.bind((serverip,port))
    server.listen(5)
    print('waiting...')

    client, addr = server.accept()
    print('connected from...',addr)

    data = client.recv(1024).decode('utf-8')
    print('Data: ',data)
    try:
        text = '{}: {} Baht'.format(data,product[data])
    except:
        text = 'no product'

    client.send(text.encode('utf-8'))
    client.close()