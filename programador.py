# -*- coding: utf-8 -*-
import json, os, sys, getpass
from termcolor import colored
from controllers.input import input_verifier
os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    from env import os
except:
    print('You havent add a env.py')

print(colored('---------------------------','green'))
print(colored('|  programador parametros |','green'))
print(colored('|   introduce tu usuario  |','green'))
print(colored('|  contraseña para acceder|','green'))
print(colored('---------------------------','green'))

count = 0
user_boolean = False
while True:
    if not user_boolean:
        user = input(colored('User: ','red'))
    if user == os.environ.get('user'):
        user_boolean = True
        password = getpass.getpass(colored('password: ','red'))
        if password == os.environ.get('password'):
            break
    count +=1
    if count > 3:
        print(colored('Se llego al limite de intentos','yellow'))
        sys.exit(1)

boot_boolean = True
while True:
    if boot_boolean:
        print(colored('--------------------------','blue'))
        print(colored('|    Iniciaste sesion    |','blue'))
        print(colored('|        CTR+C Exit      |','blue'))
        print(colored('--------------------------','blue'))
        boot_boolean = False
