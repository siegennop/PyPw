#imports
from pyperclip import copy
from sys import platform as plat
from getpass import getpass
import pickle, os
from time import sleep
import sys

dict = {}
PASSWORDS = {}
#start function block
if plat == 'win32':
    clear = 'cls'
else:
    clear = 'clear'
isFile = False

def error(err):
    print(f'Oops! Something went wrong: {err}. Please try again.')

def clearScreen():
    os.system(clear)

def showKeys(dict):
    for key in dict.keys():
        print(f'{key}\n')

def load(filename, err='OSError'):
    try:
        with open(filename, 'rb'):
            return pickle.load(filename)
    except err:
        error(err)

def save(filename, err='OSError'):
    with open(filename, 'wb'):
        pickle.dump(filename)
