import random
from os import system
from pystyle import Center
banner = r"""

__________                  __    
\______   \  ____    ____  |  | __
 |       _/ /  _ \ _/ ___\ |  |/ /
 |    |   \(  <_> )\  \___ |    < 
 |____|_  / \____/  \___  >|__|_ \
        \/              \/      \/         
                        __________                                 
                        \______   \_____   ______    ____  _______ 
                        |     ___/\__  \  \____ \ _/ __ \ \_  __ \
                        |    |     / __ \_|  |_> >\  ___/  |  | \/
                        |____|    (____  /|   __/  \___  > |__|   
                                       \/ |__|         \/         
                                                        _________        .__                                         
                                                        /   _____/  ____  |__|  ______  ______  ____  _______   ______
                                                        \_____  \ _/ ___\ |  | /  ___/ /  ___/ /  _ \ \_  __ \ /  ___/
                                                        /        \\  \___ |  | \___ \  \___ \ (  <_> ) |  | \/ \___ \ 
                                                       /_______  / \___  >|__|/____  >/____  > \____/  |__|   /____  >
                                                               \/      \/          \/      \/                      \/ 
"""
list = ['r', 'p', 's']
system('cls')
print(Center.XCenter(banner))
while True:
    print()
    eleccio_usuari = str(input(' >> Your Choice: '))
    eleccio_pc = random.choice(list)
    if eleccio_pc == 'r':
        print(' >> Pc Choice: rock')
    elif eleccio_pc == 'p':
        print(' >> Pc Choice: paper')
    elif eleccio_pc == 's':
        print(' >> Pc Choice: scissors')
    print()
    if eleccio_usuari == 'r' or eleccio_usuari == 'rock':
        if eleccio_pc == 'r':
            print('              >> Draw')
        elif eleccio_pc == 'p':
            print('              >> You Lost')
            print('----------------------------------------')
        elif eleccio_pc == 's':
            print('              >> You Won')
            print('----------------------------------------')
    elif eleccio_usuari == 'p' or eleccio_usuari == 'paper':
        if eleccio_pc == 'r':
            print('              >> You Won')
            print('----------------------------------------')
        elif eleccio_pc == 'p':
            print('              >> Draw')
        elif eleccio_pc == 's':
            print('              >> You Lost')
            print('----------------------------------------')
    elif eleccio_usuari == 's' or eleccio_usuari == 'scissors':
        if eleccio_pc == 'r':
            print('              >> You Lost')
            print('----------------------------------------')
        elif eleccio_pc == 'p':
            print('              >> You Won')
            print('----------------------------------------')
        elif eleccio_pc == 's':
            print('              >> Draw')
    else:
        print()