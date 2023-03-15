


# IMPORTS #
import os
import random
import ctypes
import time
import string
import sys
import requests
import json




########


# Variabler #
menu_art = r"""
__  __                      __        __ _                          
\ \/ /___ _ __   _____  __ / _\ ___  / _| |___      ____ _ _ __ ___ 
 \  // _ \ '_ \ / _ \ \/ / \ \ / _ \| |_| __\ \ /\ / / _` | '__/ _ \
 /  \  __/ | | | (_) >  <  _\ \ (_) |  _| |_ \ V  V / (_| | | |  __/
/_/\_\___|_| |_|\___/_/\_\ \__/\___/|_|  \__| \_/\_/ \__,_|_|  \___|
                                                                    """
print(menu_art)

options_menu = r"""
                    Discord: XenoxContact#5407
                    Telegram: XenoxContact
                    
                          Version 1.0
                          
                     |-------------------|          
                     |[?]    Gaming   [?]| 
                     |-------------------| 
                     |[1] Steam Codes    | 
                     |[2] Uplay Codes    | 
                     |[3] Origin Codes   | 
                     |-------------------|
                       
                     |-------------------|
                     |[?]  Streaming  [?]| 
                     |-------------------| 
                     |[4] Netflix        | 
                     |[5] HBO NOW        | 
                     |[6] Spotify        | 
                     |-------------------|
                     
                     |-------------------|
                     |[?] Coming soon [?]| 
                     |-------------------| 
                     |[?] *******        | 
                     |[?] *****          | 
                     |[?] *******        | 
                     |-------------------|
                    
        
 """
##########












def steam():
    #DONE
    print("[?] Please enter the amount of codes you wanna generate [?]")
    max = int(input("-> "))
    #
    counter = 0

    #
    print("[+] Generating")
    try:

        f = open("XenoxSteamCodes.txt", "w+")
    except IndexError or OSError:
        print("[-] Failed, please make sure to run the tool as admin!")
        menu()


    while counter < max:
        counter += 1

        char_set = string.ascii_uppercase + string.digits
        code1 = ''.join(random.sample(char_set * 5, 5))
        code2 = ''.join(random.sample(char_set * 5, 5))
        code3 = ''.join(random.sample(char_set * 5, 5))
        final_code = code1 + "-" + code2 + "-" + code3
        f.write(final_code)
        f.write("\n")
        ctypes.windll.kernel32.SetConsoleTitleW(f"Xenox Software | Selected [Steam] | Generated Codes [{counter}]")

    f.close()
    print("[+] Codes saved to XenoxSoftwareSteamCodes.txt")
    time.sleep(5)
    menu()


def uplay():
    #DONE
    print("[?] Please enter the amount of codes you wanna generate [?]")
    max = int(input("-> "))
    #
    counter = 0

    #
    print("[+] Generating")
    try:

        f = open("XenoxSoftwareUplayCodes.txt", "w+")
    except IndexError or OSError:
        print("[-] Failed, please make sure to run the tool as admin!")
        menu()

    while counter < max:
        counter += 1

        char_set = string.ascii_uppercase + string.digits
        code1 = ''.join(random.sample(char_set * 4, 4))
        code2 = ''.join(random.sample(char_set * 4, 4))
        code3 = ''.join(random.sample(char_set * 4, 4))
        final_code = code1 + "-" + code2 + "-" + code3
        f.write(final_code)
        f.write("\n")
        ctypes.windll.kernel32.SetConsoleTitleW(f"Xenox Software | Selected [Uplay] | Generated Codes [{counter}]")
    f.close()
    print("[+] Codes saved to XenoxSoftwareUplayCodes.txt")
    time.sleep(5)
    menu()
def origin():
    #DONE
    print("[?] Please enter the amount of codes you wanna generate [?]")
    max = int(input("-> "))
    #
    counter = 0

    #
    print("[+] Generating")
    try:

        f = open("XenoxSoftwareOrigincodes.txt", "w+")
    except IndexError or OSError:
        print("[-] Failed, please make sure to run the tool as admin!")
        print("going to menu")


    while counter < max:
        counter += 1

        char_set = string.ascii_uppercase + string.digits
        code1 = ''.join(random.sample(char_set * 4, 4))
        code2 = ''.join(random.sample(char_set * 4, 4))
        code3 = ''.join(random.sample(char_set * 4, 4))
        code4 = ''.join(random.sample(char_set * 4, 4))
        code5 = ''.join(random.sample(char_set * 4, 4))
        final_code = code1 + "-" + code2 + "-" + code3 + "-" + code4 + "-" + code5
        f.write(final_code)
        f.write("\n")
        ctypes.windll.kernel32.SetConsoleTitleW(f"Xenox Software | Selected [Origin] | Generated Codes [{counter}]")

    f.close()
    print("[+] Codes saved to XenoxSoftwareOriginCodes.txt")
    time.sleep(5)
    menu()

def netflix():
    #DONE
    print("[?] Please enter the amount of codes you wanna generate [?]")
    max = int(input("-> "))
    #
    counter = 0

    #
    print("[+] Generating")
    try:

        f = open("XenoxSoftwareNetflixCodes.txt", "w+")
    except IndexError or OSError:
        print("[-] Failed, please make sure to run the tool as admin!")
        menu()

    while counter < max:
        numlist = ["12", "13"]

        num = random.choice(numlist)
        num = int(num)
        counter += 1

        char_set = string.ascii_uppercase + string.digits
        code1 = ''.join(random.sample(char_set * num, num))

        final_code = "3" + code1
        f.write(final_code)
        f.write("\n")
        ctypes.windll.kernel32.SetConsoleTitleW(f"Xenox Software | Selected [Netflix] | Generated Codes [{counter}]")

    f.close()
    print("[+] Codes saved to XenoxSoftwareNetflixCodes.txt")
    time.sleep(5)
def hbo():
    print("[?] Please enter the amount of codes you wanna generate [?]")
    max = int(input("-> "))
    #
    counter = 0

    #
    print("[+] Generating")
    try:

        f = open("XenoxSoftwareHBONOW.txt", "w+")
    except IndexError or OSError:
        print("[-] Failed, please make sure to run the tool as admin!")
        print("going to menu")


    while counter < max:
        counter += 1

        char_set = string.digits
        code1 = ''.join(random.sample(char_set * 3, 3))
        code2 = ''.join(random.sample(char_set * 3, 3))
        code3 = ''.join(random.sample(char_set * 4, 4))
        final_code = code1 + "-" + code2 + "-" + code3
        f.write(final_code)
        f.write("\n")
        ctypes.windll.kernel32.SetConsoleTitleW(f"Xenox Software | Selected [HBO NOW] | Generated Codes [{counter}]")


    f.close()

    print("[+] Codes saved to XenoxSoftwareHBOCodes.txt")
    time.sleep(5)
    menu()
def spotify():
    #DONE
    print("[?] Please enter the amount of codes you wanna generate [?]")
    max = int(input("-> "))
    #
    counter = 0

    #
    print("[+] Generating")
    try:

        f = open("XenoxSoftwareSpotifycodes.txt", "w+")
    except IndexError or OSError:
        print("[-] Failed, please make sure to run the tool as admin!")
        print("going to menu")


    while counter < max:
        counter += 1

        char_set = string.ascii_uppercase + string.ascii_lowercase + string.digits
        code1 = ''.join(random.sample(char_set * 10, 10))

        final_code = code1
        f.write(final_code)
        f.write("\n")
        ctypes.windll.kernel32.SetConsoleTitleW(f"Xenox Software | Selected [Spotify] | Generated Codes [{counter}]")

    f.close()

    print("[+] Codes saved to XenoxSoftwareCodes.txt")
    time.sleep(5)
    menu()


### ###


# Menu #
def menu():

    print(options_menu)
    option = input("(Select a Option) -> ")
  

    if option == "1":
        steam()
    elif option == "2":
        uplay()
    elif option == "3":
        origin()
    elif option == "4":
        netflix()
    elif option == "5":
        hbo()
    elif option == "6":
        spotify()

    else:
        print("[-] Invalid input... Please try again")
        print("")
        time.sleep(5)
        menu()


menu()
