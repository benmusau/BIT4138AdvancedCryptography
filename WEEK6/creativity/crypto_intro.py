import os
import time
from datetime import datetime

# Colors
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def slow_print(text, delay=0.03, color=RESET):
    for char in text:
        print(color + char + RESET, end="", flush=True)
        time.sleep(delay)
    print()


def loading_bar():
    print(CYAN + "\n[+] Initializing Cryptographic Engine..." + RESET)
    for i in range(0, 101, 5):
        bar = "█" * (i // 5) + "-" * (20 - (i // 5))
        print(f"\r{YELLOW}[{bar}] {i}%{RESET}", end="", flush=True)
        time.sleep(0.1)
    print("\n")


def crypto_intro():
    clear()

    print(GREEN + "=" * 80 + RESET)
    print(CYAN + r"""
   ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗
  ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗
  ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║
  ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║
  ╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝
   ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝
    """ + RESET)

    print(YELLOW + "        ADVANCED CRYPTOGRAPHIC DECRYPTION AND ENCRYPTION SYSTEM" + RESET)
    print(GREEN + "=" * 80 + RESET)

    time.sleep(1)
    slow_print("[SYSTEM] Loading secure modules...", 0.04, GREEN)
    time.sleep(0.5)

    modules = [
        "Classical Cipher Module",
        "Vigenere Encryption Module",
        "AES Encryption Module",
        "RSA Key Management Module",
        "Randomness Testing Module"
    ]

    for module in modules:
        slow_print(f"[OK] {module}", 0.03, CYAN)
        time.sleep(0.3)

    loading_bar()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    slow_print("Access Granted", 0.05, GREEN)
    slow_print("Welcome Benson Musau", 0.05, YELLOW)
    slow_print("Course: BIT4138 - Advanced Cryptography", 0.03, CYAN)
    slow_print("Language: Python", 0.03, CYAN)
    slow_print(f"Date & Time: {current_time}", 0.03, CYAN)

    print(RED + "\n[!] WARNING: Unauthorized access is prohibited." + RESET)
    print(GREEN + "=" * 80 + RESET)

    input(YELLOW + "\nPress Enter to continue..." + RESET)


if __name__ == "__main__":
    crypto_intro()