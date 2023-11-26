from random import randint
from os import system, name
from colorama import Fore, Style, init

from cube import solved_cube, print_cube
from moves import horizontal_turn, vertical_turn, side_turn
from translate import translate
from playground import playground


cube = solved_cube


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def scramble(cube):
    for i in range(0, 20):
        x = randint(0, 2)
        y = randint(0, 2)
        z = randint(0, 1)
        if(x == 0):
            horizontal_turn(cube, y, z)
            print(translate("horizontal", y, z))
        elif(x == 1):
            vertical_turn(cube, y, z)
            print(translate("vertical", y, z))
        elif(x == 2):
            side_turn(cube, y, z)
            print(translate("side", y, z))


def solve(cube):
    cube = solved_cube


# Initial actions
init(autoreset = True)
choose = 0
clear()


# Main loop
while choose != 5:
    print("Co chcesz zrobić?")
    print("  1. Wyświetlić kostkę")
    print("  2. Wymieszać kostkę")
    print("  3. Ułożyć kostkę")
    print("  4. Playground")
    print("  5. Wyjść")
    choose = int(input())
    clear()
    if choose == 1:
        print_cube(cube)
    elif choose == 2:
        scramble(cube)
    elif choose == 3:
        solve(cube)
    elif choose == 4:
        playground(cube)
        clear()
    else:
        exit