import os
import time
import requests
import random
import string
import webbrowser
from colorama import Fore, init
import tkinter as tk

from tracemalloc import reset_peak

init()

reset_peak()

purple = Fore.MAGENTA
red = Fore.RED
green = Fore.GREEN
reset = Fore.RESET

session = requests.Session()
session.trust_env = False

def generate_minecraft_username(length, characters):
    return ''.join(random.choices(characters, k=length))

def minecraft(username):
    try:
        url = f"https://api.mojang.com/users/profiles/minecraft/{username.strip()}"
        r = session.get(url)

        if r.status_code == 200:
            print(f"{red}The username {username} is taken!{reset}")
        else:
            print(f"{green}The username {username} is available or locked!{reset}")
    except Exception as e:
        print(f"{purple}Failed to check username {username}: {e}{reset}")

def main():
    os.system('cls')  # Clear terminal on Windows, use 'clear' for Unix/Linux/Mac

    print(r"""{}
                         .__    .__    .___        .__                   __                 
      ___________   ____ |  |__ |__| __| _/   ____ |  |__   ____   ____ |  | __ ___________ 
     /  _ \_  __ \_/ ___\|  |  \|  |/ __ |  _/ ___\|  |  \_/ __ \_/ ___\|  |/ // __ \_  __ \\
    (  <_> )  | \/\  \___|   Y  \  / /_/ |  \  \___|   Y  \  ___/\  \___|    <\  ___/|  | \/
     \____/|__|    \___  >___|  /__\____ |   \___  >___|  /\___  >\___  >__|_ \\___  >__|   
                       \/     \/        \/       \/     \/     \/     \/     \/    \/       
    Minecraft Checker - By Orchids
    """.format(purple))

    choice = input(f"{purple}Do you want to generate usernames (gen) or get them from 'usernames.txt' (txt)? (gen/txt): {reset}")

    if choice.lower() == "gen":
        os.system('title Orchids MC Checker')

        length = int(input(f"{purple}Enter the length of the Minecraft username: {reset}"))
        characters = input(f"{purple}Enter characters to include (leave empty for alphanumeric): {reset}")
        if not characters:
            characters = string.ascii_letters + string.digits
        else:
            characters = characters.strip()

        num_usernames = int(input(f"{purple}Enter the number of usernames to generate: {reset}"))
        for _ in range(num_usernames):
            username = generate_minecraft_username(length, characters)
            minecraft(username)

    elif choice.lower() == "txt":
        file_name = 'usernames.txt'
        try:
            with open(file_name, 'r') as file:
                usernames = file.readlines()
                for username in usernames:
                    minecraft(username.strip())
        except FileNotFoundError:
            print(f"{purple}The file 'usernames.txt' was not found.{reset}")

    check_again = input(f"{purple}Do you want to check again? (yes/no): {reset}")
    if check_again.lower() == "yes":
        main()
    else:
        print(f"{purple}Thank you for using the Minecraft Checker. Goodbye!{reset}")

main()
