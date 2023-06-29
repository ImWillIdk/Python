import random
from os import system
from pystyle import Center

system('title Guess The Number - idcum')

while True:
    system('cls')

    number = random.randint(1,100)
    startingAttemps = 10
    attemps = startingAttemps
    banner = """
  _____                            __    __                                 __            
 / ___/ __ __ ___   ___  ___      / /_  / /  ___        ___  __ __  __ _   / /  ___   ____
/ (_ / / // // -_) (_-< (_-<     / __/ / _ \/ -_)      / _ \/ // / /  ' \ / _ \/ -_) / __/
\___/  \_,_/ \__/ /___//___/     \__/ /_//_/\__/      /_//_/\_,_/ /_/_/_//_.__/\__/ /_/   
                                                                                          
"""

    print(Center.XCenter(banner))
    print('\n >> Guess the number from 1 to 100\n')
    print(Center.XCenter('----------------------------------------'))
    # print(number)

    while attemps > 0:
        while True:
            try:
                guess = int(input(f' [{attemps}] >> '))
                break
            except ValueError:
                continue
        if guess == number:
            print(f'\n\n >> You guessed the number with {startingAttemps-attemps+1} attempts\n')
            print(Center.XCenter('----------------------------------------'))
            break
        elif guess > number:
            print('\n >> The number is smaller\n')
        elif guess < number:
            print('\n >> The number is bigger\n')
        attemps -= 1
    if attemps == 0:
        print(f'\n >> You lost, the number was {number}!\n')
    repeat = str(input('\n >> Keep playing? (Y/N): '))
    if repeat == str('y') or repeat == str('Y'):
        continue
    else:
        break