from cryptography.fernet import Fernet

# Key generation
key = Fernet.generate_key()
cipher = Fernet(key)

# Input
text = input("Enter text: ").encode()

# Encryption
encrypted = cipher.encrypt(text)

# Decryption
decrypted = cipher.decrypt(encrypted)

# Output
print("Key:", key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted.decode())