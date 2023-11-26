#!/usr/bin/env python3

from os import system, name
from colorama import Fore, Style, init

from cube import RubicsCube
from playground import playground


cube = RubicsCube()


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


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
        cube.print_cube()
    elif choose == 2:
        cube.scramble()
    elif choose == 3:
        cube = RubicsCube()
    elif choose == 4:
        playground(cube)
        clear()
    else:
        exit