from os import system, name

from cube import RubicsCube

def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def playground(cube):
    choose = 0
    while choose != "1":
        clear()
        cube.print_cube()
        print("Aby wyjść wybierz 1")
        choose = input()