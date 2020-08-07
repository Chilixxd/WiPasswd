#WiPasswd
#Version 1.0
#Made by: Chili
#Date: 2020-08-03
#Made in Python 3.8.1 64-bit
#Copyright Chili
#Start

import sys, os
#Varibles

helpmenu = """
Welcome to the help menu of WiPasswd

Commands:

-h Help menu.
--help Help menu.

-ss Will display all SSID's.
--ssid Will display all SSID's.

-pr Will display all devices that you have connected to.
--profile Will display all devices that you have connected to.

-pw Will display the password of the SSID you have selected
--wifipasswd Will display the password of the SSID you have selected
"""

startingtext = """
 __      __.____________                                  .___
/  \    /  \__\______   \_____    ______ ________  _  ____| _/
\   \/\/   /  ||     ___/\__  \  /  ___//  ___/\ \/ \/ / __ | 
\        /|  ||    |     / __ \_\___ \ \___ \  \     / /_/ | 
 \__/\  / |__||____|    (____  /____  >____  >  \/\_/\____ | 
      \/                     \/     \/     \/             \/ 


[+] To begin

[+] python3 WiPasswd.py -h or --help

[+] Example: python3 WiPasswd.py --ssid
Enter the SSID: test123
"""
print(startingtext) 
#Varibles

#Begining of "Flags"

if '-h' in sys.argv:
    print(helpmenu)

if '--help' in sys.argv:
    print(helpmenu)

if '-ss' in sys.argv:
    print("")
    print("")
    print("[+] Displaying all SSID's")
    print("")
    os.system('netsh wlan show networks')

if '--ssid' in sys.argv:
    print("")
    print("")
    print("[+] Displaying all SSID's")
    print("")
    os.system('netsh wlan show networks')

if '-pr' in sys.argv:
    print("") 
    print("") 
    print("[+] Displaying all devices")
    print("")
    os.system("netsh wlan show profile") 

if '--profile' in sys.argv:
    print("") 
    print("") 
    print("[+] Displaying all devices")
    print("")
    os.system('netsh wlan show profile')

if '-pw' in sys.argv:
    SSID = input("Enter the SSID: ") 
    os.system('netsh wlan show profile ' + SSID + ' key=clear')

if '--wifipasswd' in sys.argv:
    SSID = input("Enter the SSID: ")
    os.system('netsh wlan show profile ' + SSID + ' key=clear')

#Ending of "Flags"
#Ending