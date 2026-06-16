import random

# LFSR (simple simulation)
def lfsr(seed, taps, n):
    state = seed
    result = []
    for _ in range(n):
        xor = 0
        for t in taps:
            xor ^= (state >> t) & 1
        bit = state & 1
        result.append(bit)
        state = (state >> 1) | (xor << (len(seed)-1))
    return result

# RC4 simplified
def rc4(key, text):
    s = list(range(256))
    j = 0

    for i in range(256):
        j = (j + s[i] + ord(key[i % len(key)])) % 256
        s[i], s[j] = s[j], s[i]

    i = j = 0
    result = ""

    for char in text:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        k = s[(s[i] + s[j]) % 256]
        result += chr(ord(char) ^ k)

    return result

# MAIN
print("Random Sequence:", [random.randint(0,1) for _ in range(10)])

text = input("Enter text: ")
key = input("Enter key: ")

encrypted = rc4(key, text)
print("Encrypted:", encrypted)
print("Decrypted:", rc4(key, encrypted))