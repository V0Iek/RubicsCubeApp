from colorama import Fore, Style, init
from random import randint

from translate import translate

class RubicsCube:
    def __init__(self):
        self.state = [
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


    def print_row(self, side, row):
        print("".join(self.state[side][row]))

    def print_side(self, side):
        self.print_row(side, 0)
        self.print_row(side, 1)
        self.print_row(side, 2)

    def print_cube(self):
        self.print_side(0)

        print("".join(self.state[1][0]), "".join(self.state[2][0]), "".join(self.state[3][0]), "".join(self.state[4][0]))
        print("".join(self.state[1][1]), "".join(self.state[2][1]), "".join(self.state[3][1]), "".join(self.state[4][1]))
        print("".join(self.state[1][2]), "".join(self.state[2][2]), "".join(self.state[3][2]), "".join(self.state[4][2]))

        self.print_side(5)
        print("\n")


    def horizontal_turn(self, row, direction):
        if (row >= 0 and row <= 2) and (direction == 0 or direction == 1):
            if direction == 0: # Left
                self.state[1][row], self.state[2][row], self.state[3][row], self.state[4][row] = self.state[2][row], self.state[3][row], self.state[4][row], self.state[1][row]
                if row == 0:
                    self.state[0][0][0], self.state[0][0][1], self.state[0][0][2], self.state[0][1][2], self.state[0][2][2], self.state[0][2][1], self.state[0][2][0], self.state[0][1][0] = self.state[0][2][0], self.state[0][1][0], self.state[0][0][0], self.state[0][0][1], self.state[0][0][2], self.state[0][1][2], self.state[0][2][2], self.state[0][2][1]
                elif row == 2:
                    self.state[5][0][0], self.state[5][0][1], self.state[5][0][2], self.state[5][1][2], self.state[5][2][2], self.state[5][2][1], self.state[5][2][0], self.state[5][1][0] = self.state[5][0][2], self.state[5][1][2], self.state[5][2][2], self.state[5][2][1], self.state[5][2][0], self.state[5][1][0], self.state[5][0][0], self.state[5][0][1]

            elif direction == 1: # Right
                self.state[1][row], self.state[2][row], self.state[3][row], self.state[4][row] = self.state[4][row], self.state[1][row], self.state[2][row], self.state[3][row]
                if row == 0:
                    self.state[0][0][0], self.state[0][0][1], self.state[0][0][2], self.state[0][1][2], self.state[0][2][2], self.state[0][2][1], self.state[0][2][0], self.state[0][1][0] = self.state[0][0][2], self.state[0][1][2], self.state[0][2][2], self.state[0][2][1], self.state[0][2][0], self.state[0][1][0], self.state[0][0][0], self.state[0][0][1]
                elif row == 2:
                    self.state[5][0][0], self.state[5][0][1], self.state[5][0][2], self.state[5][1][2], self.state[5][2][2], self.state[5][2][1], self.state[5][2][0], self.state[5][1][0] = self.state[5][2][0], self.state[5][1][0], self.state[5][0][0], self.state[5][0][1], self.state[5][0][2], self.state[5][1][2], self.state[5][2][2], self.state[5][2][1]

    def vertical_turn(self, row, direction):
        if (row >= 0 and row <= 2) and (direction == 0 or direction == 1):
            if direction == 0: # Up
                self.state[0][0][row], self.state[0][1][row], self.state[0][2][row], self.state[1][0][row], self.state[1][1][row], self.state[1][2][row], self.state[5][0][row], self.state[5][1][row], self.state[5][2][row], self.state[3][0][row], self.state[3][1][row], self.state[3][2][row] = self.state[1][0][row], self.state[1][1][row], self.state[1][2][row], self.state[5][0][row], self.state[5][1][row], self.state[5][2][row], self.state[3][0][row], self.state[3][1][row], self.state[3][2][row], self.state[0][0][row], self.state[0][1][row], self.state[0][2][row]
                if row == 0:
                    self.state[4][0][0], self.state[4][0][1], self.state[4][0][2], self.state[4][1][2], self.state[4][2][2], self.state[4][2][1], self.state[4][2][0], self.state[4][1][0] = self.state[4][0][2], self.state[4][1][2], self.state[4][2][2], self.state[4][2][1], self.state[4][2][0], self.state[4][1][0], self.state[4][0][0], self.state[4][0][1]
                elif row == 2:
                    self.state[2][0][0], self.state[2][0][1], self.state[2][0][2], self.state[2][1][2], self.state[2][2][2], self.state[2][2][1], self.state[2][2][0], self.state[2][1][0] = self.state[2][2][0], self.state[2][1][0], self.state[2][0][0], self.state[2][0][1], self.state[2][0][2], self.state[2][1][2], self.state[2][2][2], self.state[2][2][1]
                

            elif direction == 1: # Down
                self.state[0][0][row], self.state[0][1][row], self.state[0][2][row], self.state[1][0][row], self.state[1][1][row], self.state[1][2][row], self.state[5][0][row], self.state[5][1][row], self.state[5][2][row], self.state[3][0][row], self.state[3][1][row], self.state[3][2][row] = self.state[3][0][row], self.state[3][1][row], self.state[3][2][row], self.state[0][0][row], self.state[0][1][row], self.state[0][2][row], self.state[1][0][row], self.state[1][1][row], self.state[1][2][row], self.state[5][0][row], self.state[5][1][row], self.state[5][2][row]
                if row == 0:
                    self.state[4][0][0], self.state[4][0][1], self.state[4][0][2], self.state[4][1][2], self.state[4][2][2], self.state[4][2][1], self.state[4][2][0], self.state[4][1][0] = self.state[4][2][0], self.state[4][1][0], self.state[4][0][0], self.state[4][0][1], self.state[4][0][2], self.state[4][1][2], self.state[4][2][2], self.state[4][2][1]
                elif row == 2:
                    self.state[2][0][0], self.state[2][0][1], self.state[2][0][2], self.state[2][1][2], self.state[2][2][2], self.state[2][2][1], self.state[2][2][0], self.state[2][1][0] = self.state[2][0][2], self.state[2][1][2], self.state[2][2][2], self.state[2][2][1], self.state[2][2][0], self.state[2][1][0], self.state[2][0][0], self.state[2][0][1]

    def side_turn(self, row, direction):
        if (row >= 0 and row <= 2) and (direction == 0 or direction == 1):
            if direction == 0: # Clockwise
                self.state[0][2 - row][0], self.state[0][2 - row][1], self.state[0][2 - row][2], self.state[2][0][row], self.state[2][1][row], self.state[2][2][row], self.state[5][row][0], self.state[5][row][1], self.state[5][row][2], self.state[4][0][2 - row], self.state[4][1][2 - row], self.state[4][2][2 - row] = self.state[4][2][2 - row], self.state[4][1][2 - row], self.state[4][0][2 - row], self.state[0][2 - row][0], self.state[0][2 - row][1], self.state[0][2 - row][2], self.state[2][2][row], self.state[2][1][row], self.state[2][0][row], self.state[5][row][0], self.state[5][row][1], self.state[5][row][2]
                if row == 0:
                    self.state[1][0][0], self.state[1][0][1], self.state[1][0][2], self.state[1][1][2], self.state[1][2][2], self.state[1][2][1], self.state[1][2][0], self.state[1][1][0] = self.state[1][2][0], self.state[1][1][0], self.state[1][0][0], self.state[1][0][1], self.state[1][0][2], self.state[1][1][2], self.state[1][2][2], self.state[1][2][1]
                elif row == 2:
                    self.state[3][0][0], self.state[3][0][1], self.state[3][0][2], self.state[3][1][2], self.state[3][2][2], self.state[3][2][1], self.state[3][2][0], self.state[3][1][0] = self.state[3][0][2], self.state[3][1][2], self.state[3][2][2], self.state[3][2][1], self.state[3][2][0], self.state[3][1][0], self.state[3][0][0], self.state[3][0][1]
            
            elif direction == 1: #Counter clockwise
                self.state[0][2 - row][0], self.state[0][2 - row][1], self.state[0][2 - row][2], self.state[2][0][row], self.state[2][1][row], self.state[2][2][row],self.state[5][row][0], self.state[5][row][1], self.state[5][row][2],self.state[4][0][2 - row], self.state[4][1][2 - row], self.state[4][2][2 - row] = self.state[2][0][row], self.state[2][1][row], self.state[2][2][row], self.state[5][row][2], self.state[5][row][1], self.state[5][row][0], self.state[4][0][2 - row], self.state[4][1][2 - row], self.state[4][2][2 - row], self.state[0][2 - row][2], self.state[0][2 - row][1], self.state[0][2 - row][0]
                if row == 0:
                    self.state[1][0][0], self.state[1][0][1], self.state[1][0][2], self.state[1][1][2], self.state[1][2][2], self.state[1][2][1], self.state[1][2][0], self.state[1][1][0] = self.state[1][0][2], self.state[1][1][2], self.state[1][2][2], self.state[1][2][1], self.state[1][2][0], self.state[1][1][0], self.state[1][0][0], self.state[1][0][1]
                elif row == 2:
                    self.state[3][0][0], self.state[3][0][1], self.state[3][0][2], self.state[3][1][2], self.state[3][2][2], self.state[3][2][1], self.state[3][2][0], self.state[3][1][0] = self.state[3][2][0], self.state[3][1][0], self.state[3][0][0], self.state[3][0][1], self.state[3][0][2], self.state[3][1][2], self.state[3][2][2], self.state[3][2][1]


    def scramble(self):
        for i in range(0, 20):
            x = randint(0, 2)
            y = randint(0, 2)
            z = randint(0, 1)
            if x == 0:
                self.horizontal_turn(y, z)
                print(translate("horizontal", y, z))
            elif x == 1:
                self.vertical_turn(y, z)
                print(translate("vertical", y, z))
            elif x == 2:
                self.side_turn(y, z)
                print(translate("side", y, z))