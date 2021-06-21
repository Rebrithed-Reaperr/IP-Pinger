import colorama, time, os, system
from colorama import Fore
from time import sleep

Offline_Logo = f"""
{Fore.RED}╔═╗╔═╗╔═╗╦  ╦╔╗╔╔═╗
{Fore.RED}║ ║╠╣ ╠╣ ║  ║║║║║╣ 
{Fore.RED}╚═╝╚  ╚  ╩═╝╩╝╚╝╚═╝
"""

Online_Logo = f"""
{Fore.GREEN}╔═╗╔╗╔╦  ╦╔╗╔╔═╗
{Fore.GREEN}║ ║║║║║  ║║║║║╣ 
{Fore.GREEN}╚═╝╝╚╝╩═╝╩╝╚╝╚═╝
"""

Main_Logo = f"""
{Fore.CYAN}╔═╗┬┌┐┌┌─┐┌─┐┬─┐
{Fore.CYAN}╠═╝│││││ ┬├┤ ├┬┘
{Fore.CYAN}╩  ┴┘└┘└─┘└─┘┴└─
"""

os.system('cls')

def ping():
    while True:
        ping_response = os.system(f'ping -n 1 <ip> <nul')
        if ping_response == 0:
            os.system('cls')
            print(Main_Logo)
            print(Online_Logo)
            time.sleep(0.1)
              os.system('cls')
              print(Main_Logo)
              print(Offline_Logo)
              time.sleep(0.1)
os.system('title Welcome To My Pinger...')

print(Main_Logo)
ip = input('Enter A IP/Domain: ')
ping()
