from pdb import Restart
from weakref import proxy
import requests
import ctypes
import time
from threading import Thread
from colorama import Fore, Back, Style
import random
import os

ctypes.windll.kernel32.SetConsoleTitleW(f"[GITHUB USERNAME CHECKER]")

usernames = open("data/usernames.txt", "r").read().splitlines()
proxies = open("data/proxies.txt", "r").read().splitlines()
checked_ = 0
checked = []
proxytype = None

def filter_names(names: list): 
    output = [] 
    for name in names:
        if name in output: 
            continue 
        output.append(name) 
    return output 

usernames = filter_names(usernames) 

class github:
    def check(username, proxy, proxytype):
        global checked_, proxies, checked
        if username in checked:
            return print(Fore.RED + "[Already Checked]" + Fore.RESET + " | " + username + " | " + proxy)
        proxies_ = {f'{proxytype}': f'{proxytype}://' + proxy}
        r = requests.get(f'https://github.com/{username}', proxies=proxies_)
        time.sleep(delay)
        if r.status_code == 200:
            print(Fore.RED + "[Username Taken]" + Fore.RESET + " | " + username + " | " + proxy)
        elif r.status_code == 404:
            print(Fore.GREEN + "[Username Free]" + Fore.RESET + " | " + username + " | " + proxy)
            checked_ += 1
            ctypes.windll.kernel32.SetConsoleTitleW(f"[GITHUB USERNAME CHECKER] |  %s" % checked_ + ' FREE')
            with open ("data/available.txt", "a+") as file:
                file.write(username + "\n")
        else:
            print(Fore.RED + "[Ratelimit]" + Fore.RESET + " | " + username + " | " + proxy)        
        checked.append(username)
        time.sleep(5)

    def check2(username):
        global checked_
        if username in checked:
            return print(Fore.RED + "[Already Checked]" + Fore.RESET + " | " + username)
        r = requests.get(f'https://github.com/{username}')
        if r.status_code == 200:
            print(Fore.RED + "[Username Taken]" + Fore.RESET + " | " + username)
        elif r.status_code == 404:
            print(Fore.GREEN + "[Username Free]" + Fore.RESET + " | " + username)
            checked_ += 1
            ctypes.windll.kernel32.SetConsoleTitleW(f"[GITHUB USERNAME CHECKER] |  %s" % checked_ + ' FREE')
            with open ("data/available.txt", "a+") as file:
                file.write(username + "\n")
        else:
            print(Fore.RED + "[Ratelimit]" + Fore.RESET + " | " + username)      
        checked.append(username)  
        time.sleep(5)

def startup():
    for username in usernames: 
            time.sleep(delay)
            Thread(target=github.check, args=[username, random.choice(proxies), proxytype]).start()

def startup2():
    for username in usernames: 
                time.sleep(delay)
                Thread(target=github.check2, args=[username]).start()

def proxytime():
    global proxytype
    global delay

    delay = input(Fore.RED + '[?]' + Fore.RESET + ' Delay >> ')
    delay = int(delay)
    delay = delay / 1000
    wannaproxy = input(Fore.RED + '[?]' + Fore.RESET + ' Use Proxies >> ')
    if wannaproxy.lower() == "yes" or wannaproxy.lower() == "y":
        huh = input(Fore.RED + '[?]' + Fore.RESET + ' Proxy Type >> ')
        if huh == 'socks4':
            os.system('cls')
            startup()
            proxytype = 'socks4'
        elif huh == 'socks5':
            os.system('cls')
            startup()
            proxytype = 'socks5'
        elif huh == 'http':
            os.system('cls')
            startup()
            proxytype = 'http'
        elif huh == 'https':
            os.system('cls')
            startup()
            proxytype = 'https'
        else:
            os.system('cls')
            print(Fore.RED + '[!]' + Fore.RESET + ' Invalid Proxy Type')
            proxytime()          
    elif wannaproxy.lower() == "no" or wannaproxy.lower() == "n":
        startup2()
        os.system('cls')
    else:
        os.system('cls')
        print(Fore.RED + '[!]' + Fore.RESET + ' Invalid Option')
        proxytime()

if __name__ == '__main__':
    with open ("data/available.txt", "w") as file:
        file.write('') # Clears file
    os.system('cls')
    proxytime()
            
