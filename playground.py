from os import system, name

from cube import print_cube
from moves import horizontal_turn, vertical_turn, side_turn

def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def playground(cube):
    choose = 0
    while choose != "1":
        clear()
        print_cube(cube)
        print("Aby wyjść wybierz 1")
        choose = input()