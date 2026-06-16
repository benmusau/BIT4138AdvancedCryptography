from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

message = b"Hello World"
encrypted = f.encrypt(message)
decrypted = f.decrypt(encrypted)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)