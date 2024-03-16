# https://shorturl.at/fgLQV
# https://rb.gy/ju2b1
# https://n9.cl/1ipjk

import os
import requests
from colorama import Fore

os.system("cls")
os.system("title URL Checker  /  t.me/rei07x")


url = input(f"[{Fore.CYAN}?{Fore.RESET}] Enter URL: ")

try:
    req = requests.get(url, allow_redirects=True)
    print(f"[{Fore.CYAN}+{Fore.RESET}] The real URL Is : {req.url}")
except:
    print(f"[{Fore.RED}~{Fore.RESET}] Error")
