import socket
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
root.title("Secure Client")

tk.Label(root, text="Message:").pack()

entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

output = tk.Text(root, width=60, height=15)
output.pack(padx=10, pady=10)

def log(msg):
    output.insert(tk.END, msg + "\n")
    output.see(tk.END)

def send_message():
    message = entry.get()
    if not message:
        return

    try:
        client = socket.socket()
        client.connect((SERVER_IP, PORT))

        encrypted_msg = cipher.encrypt(message.encode())
        client.send(encrypted_msg)
        log(f"📤 Sent (encrypted): {encrypted_msg}")

        response = client.recv(1024)
        decrypted_response = cipher.decrypt(response).decode()
        log(f"📥 Server replied: {decrypted_response}\n")

        client.close()
        entry.delete(0, tk.END)

    except Exception as e:
        log(f"❌ Error: {e}")

tk.Button(root, text="Send", command=send_message).pack(pady=5)

root.mainloop()
