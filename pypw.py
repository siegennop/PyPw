#imports

from sys import platform as plat
from getpass import getpass
import pickle, os
from pprint import pprint, pformat
from time import sleep
#start function block
if plat == 'win32':
    clear = 'cls'
else:
    clear = 'clear'
isFile = False

def error():
    print('Oops! Something went wrong.')
    return

def clearScreen():
    os.system(clear)

def showKeys(dict):
    pprint(dict.keys())

def saveData(data, filename='passwords.p'):
    try:
        with open(filename, 'wb'):
            pickle.dump(data, filename)
    except OSError as err:
        print(f'Oops! Something went wrong: {err}')

def loadData(data, filename='passwords.p'):
    try:
        global isFile
        with open(filename, 'rb'):
            employees = pickle.load(filename)
        isFile = True
    except OSError as err:
        print(f'Oops! Something went wrong: {err}')
#end function block

choice = 0

passwords = {}

while choice != 'q':
    clearScreen()
    #main screen
    print('Hello! Welcome to Python Passwords. Select one of the options below to get started:')
    print('\'a\' - add accounts and passwords, either to the existing file or to a new file.')
    print('\'c\' - show credits.')
    if isFile == True:
        print('\'d\' - delete existing accounts and passwords.')
        print('\'e\' - edit your existing accounts and passwords.')
    print('\'l\' - load data from a file. (Note: you will have needed to save a file beforehand.)')
    print('\'s\' - shows accounts, which you can copy the passwords from.')
    print('\'q\' - saves and quits. (Note: if you haven\'t specified a filename, it will save as passwords.p).')

    choice = input()
    #start if
    if choice == 'a':
        key = input('Enter your account (e.g. email, blog etc.): ')
        password = getpass('Enter your password: ')
        passwords[key] = password
    elif choice == 'c':
        print('This script was written by A***** P**** of S** Middle School.\nYou can contact him by email (popova@esms.org.uk) or by Discord (dankmemesarenoice#2929).\n\nYou can find this code on GitHub: https://github.com/sung0esd0wn/PyPw\nPull requests are appreciated.')
        input('Press Enter to continue...')
    elif choice
