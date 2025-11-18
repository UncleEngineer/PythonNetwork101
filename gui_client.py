from tkinter import *
from tkinter import ttk # theme of Tk
########################
import socket
import threading
############FROM SERVER##############
serverip = '10.25.12.131'
port = 8500


def send_message(data):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    server.connect((serverip,port))
    server.send(data.encode('utf-8'))

    data_server = server.recv(1024).decode('utf-8')
    print('Data from server: ',data_server)
    v_result.set(data_server)
    server.close()
    

########################



GUI = Tk()
GUI.title('Product Price Checker')
GUI.geometry('600x400')

L1 = Label(GUI,text='โปรแกรมตรวจสอบราคา',font=(None,20))
L1.pack()

v_textbox = StringVar()
E1 = ttk.Entry(GUI,textvariable=v_textbox, width=50,font=('Angsana New',20,'bold'))
E1.pack(pady=20)

def senddata():
    # product = {'mango':20,'banana':30}
    textbox = v_textbox.get()
    # output = product[textbox]
    # text = '{}: {} baht'.format(textbox,output)
    task1 = threading.Thread(target=send_message,args=[textbox])
    task1.start()



B1 = ttk.Button(GUI,text='Send',command=senddata)
B1.pack(ipadx=30,ipady=20)

v_result = StringVar()
v_result.set('--------Result--------')
LR1 = Label(GUI,textvariable=v_result,font=('Angsana New',30,'bold'))
LR1.pack(pady=20)

GUI.mainloop()