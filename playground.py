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
        if choose == "L":
            cube.vertical_turn(0, 1)
        elif choose == "L'":
            cube.vertical_turn(0, 0)
        elif choose == "M":
            cube.vertical_turn(1, 1)
        elif choose == "M'":
            cube.vertical_turn(1, 0)
        elif choose == "R":
            cube.vertical_turn(2, 0)
        elif choose == "R'":
            cube.vertical_turn(2, 1)