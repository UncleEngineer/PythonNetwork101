import socket
import threading
import tkinter as tk
from cryptography.fernet import Fernet

# ====== CIPHER ======
with open('secret.key', 'rb') as f:
    key = f.read()

cipher = Fernet(key)

# ====== SERVER CONFIG ======
SERVER_IP = '192.168.100.234'
PORT = 8500

# ====== GUI ======
root = tk.Tk()
root.title("Secure Server")

text_area = tk.Text(root, width=60, height=20)
text_area.pack(padx=10, pady=10)

def log(msg):
    text_area.insert(tk.END, msg + "\n")
    text_area.see(tk.END)

def start_server():
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((SERVER_IP, PORT))
    server.listen(5)

    log("🟢 Server started...")
    log(f"Listening on {SERVER_IP}:{PORT}")

    while True:
        client, addr = server.accept()
        log(f"🔗 Connected from {addr}")

        data = client.recv(1024)
        log(f"Encrypted data: {data}")

        decrypted = cipher.decrypt(data).decode()
        log(f"Decrypted message: {decrypted}")

        response = "Got the secret text"
        encrypted_response = cipher.encrypt(response.encode())
        client.send(encrypted_response)

        client.close()
        log("❌ Client disconnected\n")

# run server in background thread
threading.Thread(target=start_server, daemon=True).start()

root.mainloop()
