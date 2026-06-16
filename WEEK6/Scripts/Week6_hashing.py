import hashlib

# Register password
password = input("Create password: ")
hashed_password = hashlib.sha256(password.encode()).hexdigest()
print("Stored Hash:", hashed_password)

# Login verification
login = input("Enter password to login: ")
login_hash = hashlib.sha256(login.encode()).hexdigest()

if login_hash == hashed_password:
    print("Login successful")
else:
    print("Login failed")