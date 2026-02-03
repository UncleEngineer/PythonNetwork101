from cryptography.fernet import Fernet

with open('secret.key','rb') as f:
    key = f.read()

cipher = Fernet(key)

encrypted_msg = b'gAAAAABpge-CR0KK0uFBHc_06N3b1X9YKFNcZPEk_A9G5tR3kMMMfyGaAoPzZ3X3gfn7zVfGeuZxxK1tUT-qCv0fvNOmJ7aLVWpqrsa3hxlBBgyEgzzO-JatW7audaUyIjfOUKoyFRuM'
decrypted = cipher.decrypt(encrypted_msg).decode(encoding='utf-8')

print('Decrypted: ',decrypted)
