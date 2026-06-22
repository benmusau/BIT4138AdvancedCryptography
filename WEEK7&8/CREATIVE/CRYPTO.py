#!/usr/bin/env python3
"""
banner.py
Alternative crypto-style terminal banner
No external libraries required.
"""

from datetime import datetime


# ANSI colors
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def crypto_banner():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(GREEN + "=" * 80 + RESET)
    print(CYAN + r"""
     █████╗ ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗ ██████╗███████╗██████╗
    ██╔══██╗██╔══██╗██║   ██║██╔══██╗████╗  ██║██╔════╝██╔════╝██╔══██╗
    ███████║██║  ██║██║   ██║███████║██╔██╗ ██║██║     █████╗  ██████╔╝
    ██╔══██║██║  ██║╚██╗ ██╔╝██╔══██║██║╚██╗██║██║     ██╔══╝  ██╔══██╗
    ██║  ██║██████╔╝ ╚████╔╝ ██║  ██║██║ ╚████║╚██████╗███████╗██║  ██║
    ╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═╝  ╚═╝
    """ + RESET)

    print(YELLOW + "              DECRYPTION AND ENCRYPTION SYSTEM" + RESET)
    print(GREEN + "=" * 80 + RESET)
    print(f"{CYAN} Course   : BIT4138 - Advanced Cryptography{RESET}")
    print(f"{CYAN} Author   : Benson Musau{RESET}")
    print(f"{CYAN} Language : Python{RESET}")
    print(f"{CYAN} Time     : {current_time}{RESET}")
    print(GREEN + "-" * 80 + RESET)
    print(f"{YELLOW} Modules  : Classical Ciphers | Stream Ciphers | AES | RSA{RESET}")
    print(f"{YELLOW} Status   : Secure System Initialized{RESET}")
    print(GREEN + "=" * 80 + RESET)
    print()


if __name__ == "__main__":
    crypto_banner()