import os
import json
import base64
import hashlib
from cryptography.fernet import Fernet

USER_FILE = "vault_user.json"
NOTE_FILE = "secret_note.bin"

# Hash password
def hash_password(password, salt):
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000).hex()

# Create encryption key from password
def derive_key(password, salt):
    key = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000, dklen=32)
    return base64.urlsafe_b64encode(key)

# Register user
def register():
    print("\n=== FIRST TIME SETUP ===")
    password = input("Create master password: ")
    salt = os.urandom(16)

    user_data = {
        "salt": salt.hex(),
        "password_hash": hash_password(password, salt)
    }

    with open(USER_FILE, "w") as f:
        json.dump(user_data, f)

    print("Vault created successfully!\n")
    return password, user_data

# Load user data
def load_user():
    with open(USER_FILE, "r") as f:
        return json.load(f)

# Login
def login(user_data):
    salt = bytes.fromhex(user_data["salt"])

    for attempt in range(3):
        password = input("Enter master password: ")
        if hash_password(password, salt) == user_data["password_hash"]:
            print("Login successful!\n")
            return password
        else:
            print("Wrong password.\n")

    print("Too many failed attempts. Exiting.")
    return None

# Save encrypted note
def save_note(cipher):
    note = input("Enter your secret note: ")
    encrypted_note = cipher.encrypt(note.encode())

    with open(NOTE_FILE, "wb") as f:
        f.write(encrypted_note)

    print("Note encrypted and saved successfully!\n")

# Read encrypted note
def read_note(cipher):
    if not os.path.exists(NOTE_FILE):
        print("No secret note found.\n")
        return

    with open(NOTE_FILE, "rb") as f:
        encrypted_note = f.read()

    try:
        decrypted_note = cipher.decrypt(encrypted_note).decode()
        print("Decrypted Note:", decrypted_note, "\n")
    except:
        print("Decryption failed.\n")

# Menu
def menu(cipher):
    while True:
        print("=== SECURE NOTE VAULT ===")
        print("1. Save Secret Note")
        print("2. Read Secret Note")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            save_note(cipher)
        elif choice == "2":
            read_note(cipher)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")

# Main
def main():
    if not os.path.exists(USER_FILE):
        password, user_data = register()
    else:
        user_data = load_user()
        password = login(user_data)
        if password is None:
            return

    salt = bytes.fromhex(user_data["salt"])
    key = derive_key(password, salt)
    cipher = Fernet(key)

    menu(cipher)

if __name__ == "__main__":
    main()