import socket

product = {'apple':50,'banana':30,'mango':20}
pw = ['ABC007','XYZ999']
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

    check = data.split('_') # ['ABC007','mango']

    if check[0] in pw:
        text = 'Hi, {}\n{}: {} Baht'.format(check[0],check[1],product[check[1]])
    else:
        text = 'Please Enter The Officer Code >>>'

    client.send(text.encode('utf-8'))
    client.close()