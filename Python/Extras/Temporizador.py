import time
import os
import sys

def countdown(num_of_secs):
    while num_of_secs:
        os.system("clear")
        print("Conteo \n")
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format)
        time.sleep(1)
        num_of_secs -=1
    os.system("clear")
    print('Countdown finished')
    system = os.uname()
    if system.sysname == 'Linux':
        print(system)
    if sys.platform == 'win32':
        print('1')
    elif sys.platform == 'linux':
        print('0')
        os.system('sudo su')
        if os.getlogin() == 'root':
            os.system('whoami')

inp = input("Ingresa un número para iniciar el temporizador: ")
countdown(int(inp))