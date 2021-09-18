from colorama import *
from art import *
import os, threading, time

info = f"[{Fore.BLUE}INFO{Fore.RESET}] - "
good = f"[{Fore.GREEN}+{Fore.RESET}] - "
bad = f"[{Fore.GREEN}/{Fore.RESET}] - "

try:
    os.system('title SuperPinger')
except:
    pass

banner = f"""
   _____                       ____  _                      
  / ___/__  ______  ___  _____/ __ \(_)___  ____ ____  _____
  \__ \/ / / / __ \/ _ \/ ___/ /_/ / / __ \/ __ `/ _ \/ ___/
 ___/ / /_/ / /_/ /  __/ /  / ____/ / / / / /_/ /  __/ /    
/____/\__,_/ .___/\___/_/  /_/   /_/_/ /_/\__, /\___/_/     
          /_/                            /____/ 
                {Fore.BLUE}Goku_ByMcDo/Ms{Fore.RESET}
                {Fore.BLUE}Simple Pinger {Fore.RESET}         
"""
def timer():
    print(good+"3")
    time.sleep(1)
    print(good+"2")
    time.sleep(1)
    print(good+"1")



def clear():
    try:
        os.system('cls')
    except:
        os.system('clear')

def pinger():
    ip = input(f'[{Fore.BLUE}INFO{Fore.RESET}] - IP > ')
    print('')
    print(good+"Start in 3s")
    timer()
    time.sleep(0.5)
    print(good+"Starting")

    try:
        while True:
            os.system('ping '+ip)
            print('')
            print(good+'Ping Successful')
            time.sleep(1)
    except:
        print(bad+"An error has appeared, return to the menu in 3s")
        timer()
        return affichage()


def threader():
    thread = threading.Thread(target=pinger)
    thread.start()

def affichage():
    clear()
    print(Fore.RED+banner+Fore.RESET)
    threader()

affichage()
