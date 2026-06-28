import hashlib
import itertools
import time

# Weak password for safe lab testing
password = "123"
hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("Stored SHA-256 Hash:", hashed_password)

# Brute force attack simulation
start = time.time()
characters = "0123456789"
found = False

for guess in itertools.product(characters, repeat=3):
    attempt = ''.join(guess)
    attempt_hash = hashlib.sha256(attempt.encode()).hexdigest()

    if attempt_hash == hashed_password:
        print("Password cracked:", attempt)
        found = True
        break

end = time.time()

print("Attack Time:", round(end - start, 4), "seconds")

# Weak key analysis
weak_keys = ["123", "000", "111", "password", "admin"]

print("\nWeak Key Analysis:")
if password in weak_keys:
    print("Weak password detected. Recommendation: Use longer and complex passwords.")
else:
    print("Password is stronger.")