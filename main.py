from random import randint
from os import system, name
from colorama import Fore, Style, init


cube = [
    [
        [f"{Fore.WHITE}W{Style.RESET_ALL}", f"{Fore.WHITE}W{Style.RESET_ALL}", f"{Fore.WHITE}W{Style.RESET_ALL}"],
        [f"{Fore.WHITE}W{Style.RESET_ALL}", f"{Fore.WHITE}W{Style.RESET_ALL}", f"{Fore.WHITE}W{Style.RESET_ALL}"],
        [f"{Fore.WHITE}W{Style.RESET_ALL}", f"{Fore.WHITE}W{Style.RESET_ALL}", f"{Fore.WHITE}W{Style.RESET_ALL}"]
    ],
    [
        [f"{Fore.BLUE}B{Style.RESET_ALL}", f"{Fore.BLUE}B{Style.RESET_ALL}", f"{Fore.BLUE}B{Style.RESET_ALL}"],
        [f"{Fore.BLUE}B{Style.RESET_ALL}", f"{Fore.BLUE}B{Style.RESET_ALL}", f"{Fore.BLUE}B{Style.RESET_ALL}"],
        [f"{Fore.BLUE}B{Style.RESET_ALL}", f"{Fore.BLUE}B{Style.RESET_ALL}", f"{Fore.BLUE}B{Style.RESET_ALL}"]
    ],
    [
        [f"{Fore.MAGENTA}O{Style.RESET_ALL}", f"{Fore.MAGENTA}O{Style.RESET_ALL}", f"{Fore.MAGENTA}O{Style.RESET_ALL}"],
        [f"{Fore.MAGENTA}O{Style.RESET_ALL}", f"{Fore.MAGENTA}O{Style.RESET_ALL}", f"{Fore.MAGENTA}O{Style.RESET_ALL}"],
        [f"{Fore.MAGENTA}O{Style.RESET_ALL}", f"{Fore.MAGENTA}O{Style.RESET_ALL}", f"{Fore.MAGENTA}O{Style.RESET_ALL}"]
    ],
    [
        [f"{Fore.GREEN}G{Style.RESET_ALL}", f"{Fore.GREEN}G{Style.RESET_ALL}", f"{Fore.GREEN}G{Style.RESET_ALL}"],
        [f"{Fore.GREEN}G{Style.RESET_ALL}", f"{Fore.GREEN}G{Style.RESET_ALL}", f"{Fore.GREEN}G{Style.RESET_ALL}"],
        [f"{Fore.GREEN}G{Style.RESET_ALL}", f"{Fore.GREEN}G{Style.RESET_ALL}", f"{Fore.GREEN}G{Style.RESET_ALL}"]
    ],
    [
        [f"{Fore.RED}R{Style.RESET_ALL}", f"{Fore.RED}R{Style.RESET_ALL}", f"{Fore.RED}R{Style.RESET_ALL}"],
        [f"{Fore.RED}R{Style.RESET_ALL}", f"{Fore.RED}R{Style.RESET_ALL}", f"{Fore.RED}R{Style.RESET_ALL}"],
        [f"{Fore.RED}R{Style.RESET_ALL}", f"{Fore.RED}R{Style.RESET_ALL}", f"{Fore.RED}R{Style.RESET_ALL}"]
    ],
    [
        [f"{Fore.YELLOW}Y{Style.RESET_ALL}", f"{Fore.YELLOW}Y{Style.RESET_ALL}", f"{Fore.YELLOW}Y{Style.RESET_ALL}"],
        [f"{Fore.YELLOW}Y{Style.RESET_ALL}", f"{Fore.YELLOW}Y{Style.RESET_ALL}", f"{Fore.YELLOW}Y{Style.RESET_ALL}"],
        [f"{Fore.YELLOW}Y{Style.RESET_ALL}", f"{Fore.YELLOW}Y{Style.RESET_ALL}", f"{Fore.YELLOW}Y{Style.RESET_ALL}"]
    ]
]


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def print_row(cube, side, row):
    print("".join(cube[side][row]))

def print_side(cube, side):
    print_row(cube, side, 0)
    print_row(cube, side, 1)
    print_row(cube, side, 2)

def print_cube(cube):
    print_side(cube, 0)

    print("".join(cube[1][0]), "".join(cube[2][0]), "".join(cube[3][0]), "".join(cube[4][0]))
    print("".join(cube[1][1]), "".join(cube[2][1]), "".join(cube[3][1]), "".join(cube[4][1]))
    print("".join(cube[1][2]), "".join(cube[2][2]), "".join(cube[3][2]), "".join(cube[4][2]))

    print_side(cube, 5)
    print("\n")


def horizontal_turn(cube, row, direction):
    if (row >= 0 and row <= 2) and (direction == 0 or direction == 1):
        if direction == 0: # Left
            cube[1][row], cube[2][row], cube[3][row], cube[4][row] = cube[2][row], cube[3][row], cube[4][row], cube[1][row]
        elif direction == 1: # Right
            cube[1][row], cube[2][row], cube[3][row], cube[4][row] = cube[4][row], cube[1][row], cube[2][row], cube[3][row]

def vertical_turn(cube, row, direction):
    if (row >= 0 and row <= 2) and (direction == 0 or direction == 1):
        if direction == 0: # Up
            cube[0][0][row], cube[0][1][row], cube[0][2][row], cube[1][0][row], cube[1][1][row], cube[1][2][row], cube[5][0][row], cube[5][1][row], cube[5][2][row], cube[3][0][row], cube[3][1][row], cube[3][2][row] = cube[1][0][row], cube[1][1][row], cube[1][2][row], cube[5][0][row], cube[5][1][row], cube[5][2][row], cube[3][0][row], cube[3][1][row], cube[3][2][row], cube[0][0][row], cube[0][1][row], cube[0][2][row]
        elif direction == 1: # Down
            cube[0][0][row], cube[0][1][row], cube[0][2][row], cube[1][0][row], cube[1][1][row], cube[1][2][row], cube[5][0][row], cube[5][1][row], cube[5][2][row], cube[3][0][row], cube[3][1][row], cube[3][2][row] = cube[3][0][row], cube[3][1][row], cube[3][2][row], cube[0][0][row], cube[0][1][row], cube[0][2][row], cube[1][0][row], cube[1][1][row], cube[1][2][row], cube[5][0][row], cube[5][1][row], cube[5][2][row]

def side_turn(cube, row, direction):
    if (row >= 0 and row <= 2) and (direction == 0 or direction == 1):
        if direction == 0: # Clockwise
            cube[0][2 - row][0], cube[0][2 - row][1], cube[0][2 - row][2], cube[2][0][row], cube[2][1][row], cube[2][2][row], cube[5][row][0], cube[5][row][1], cube[5][row][2], cube[4][0][2 - row], cube[4][1][2 - row], cube[4][2][2 - row] = cube[4][0][2 - row], cube[4][1][2 - row], cube[4][2][2 - row], cube[0][2 - row][0], cube[0][2 - row][1], cube[0][2 - row][2], cube[2][0][row], cube[2][1][row], cube[2][2][row], cube[5][row][0], cube[5][row][1], cube[5][row][2]
        elif direction == 1: #Counter clockwise
            cube[0][2 - row][0], cube[0][2 - row][1], cube[0][2 - row][2], cube[2][0][row], cube[2][1][row], cube[2][2][row], cube[5][row][0], cube[5][row][1], cube[5][row][2], cube[4][0][2 - row], cube[4][1][2 - row], cube[4][2][2 - row] = cube[2][0][row], cube[2][1][row], cube[2][2][row], cube[5][row][0], cube[5][row][1], cube[5][row][2], cube[4][0][2 - row], cube[4][1][2 - row], cube[4][2][2 - row], cube[0][2 - row][0], cube[0][2 - row][1], cube[0][2 - row][2]


def scramble(cube):
    for i in range(0, 20):
        x = randint(0, 2)
        y = randint(0, 2)
        z = randint(0, 1)
        if(x == 0):
            horizontal_turn(cube, y, z)
            print("Horizontal " + str(y) + " " + str(z))
        elif(x == 1):
            vertical_turn(cube, y, z)
            print("Vertical " + str(y) + " " + str(z))
        elif(x == 2):
            side_turn(cube, y, z)
            print("Side " + str(y) + " " + str(z))

#def solve(cube):

def playground():
    choose1 = 0
    while choose1 != "1":
        clear()
        print_cube(cube)
        print("Aby wyjść wybierz 1")
        choose1 = input()


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
    #elif choose == 3:
        #solve(cube)
    elif choose == 4:
        playground()
        clear()
    else:
        exit