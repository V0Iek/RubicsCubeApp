from random import randint


cube = [
    [   # Top = 0
        [["W"], ["W"], ["W"]],
        [["W"], ["W"], ["W"]],
        [["W"], ["W"], ["W"]]
    ],
    [ # Front = 1
        [["B"], ["B"], ["B"]],
        [["B"], ["B"], ["B"]],
        [["B"], ["B"], ["B"]]
    ],
    [ # Right = 2
        [["O"], ["O"], ["O"]],
        [["O"], ["O"], ["O"]],
        [["O"], ["O"], ["O"]]
    ],
    [ # Back = 3
        [["G"], ["G"], ["G"]],
        [["G"], ["G"], ["G"]],
        [["G"], ["G"], ["G"]]
    ],
    [ # Left = 4
        [["R"], ["R"], ["R"]],
        [["R"], ["R"], ["R"]],
        [["R"], ["R"], ["R"]]
    ],
    [ # Bottom = 5
        [["Y"], ["Y"], ["Y"]],
        [["Y"], ["Y"], ["Y"]],
        [["Y"], ["Y"], ["Y"]]
    ]
]


def print_row(cube, side, row):
    print(cube[side][row][0] + cube[side][row][1] + cube[side][row][2])

def print_side(cube, side):
    print_row(cube, side, 0)
    print_row(cube, side, 1)
    print_row(cube, side, 2)

def print_cube(cube):
    print_side(cube, 0)

    print(cube[1][0], cube[2][0], cube[3][0], cube[4][0])
    print(cube[1][1], cube[2][1], cube[3][1], cube[4][1])
    print(cube[1][2], cube[2][2], cube[3][2], cube[4][2])

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

def solve(cube):
    if cube[0][1][1] != ["W"]:
        if cube[1][1][1] == ["W"]:
            vertical_turn(cube, 1, 0)
        elif cube[3][1][1]:
            vertical_turn(cube, 1, 0)
            vertical_turn(cube, 1, 0)


vertical_turn(cube, 1, 1)
print_cube(cube)
solve(cube)
print_cube(cube)

# choose = 0
# while choose != 4:
#     print("Co chcesz zrobić?")
#     print("  1. Wyświetlić kostkę")
#     print("  2. Wymieszać kostkę")
#     print("  3. Ułożyć kostkę")
#     print("  4. Wyjść")
#     choose = input()
#     if choose == 1:
#         print_cube(cube)
#     elif choose == 2:
#         scramble(cube)
#     elif choose == 3:
#         solve(cube)
#     else:
#         pass