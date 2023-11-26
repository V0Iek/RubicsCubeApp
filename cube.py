from colorama import Fore, Style, init
from random import randint

from moves import horizontal_turn, vertical_turn, side_turn
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

    def scramble(self):
        for i in range(0, 20):
            x = randint(0, 2)
            y = randint(0, 2)
            z = randint(0, 1)
            if x == 0:
                horizontal_turn(self.state, y, z)
                print(translate("horizontal", y, z))
            elif x == 1:
                vertical_turn(self.state, y, z)
                print(translate("vertical", y, z))
            elif x == 2:
                side_turn(self.state, y, z)
                print(translate("side", y, z))