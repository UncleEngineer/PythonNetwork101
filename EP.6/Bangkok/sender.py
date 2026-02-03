from cryptography.fernet import Fernet

with open('secret.key','rb') as f:
    key = f.read()

cipher = Fernet(key)

message = 'สวัสดีจ้าาา'

encrypted = cipher.encrypt(message.encode(encoding='utf-8'))

print(encrypted)