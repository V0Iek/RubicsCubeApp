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