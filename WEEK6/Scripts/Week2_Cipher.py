# Caesar Cipher
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Vigenère Cipher
def vigenere_encrypt(text, key):
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - 97
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            key_index += 1
        else:
            result += char
    return result

# MAIN
text = input("Enter text: ")
shift = int(input("Enter shift (Caesar): "))
key = input("Enter key (Vigenère): ")

print("Original:", text)
print("Encrypted:", caesar_encrypt(text, shift))