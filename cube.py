from colorama import Fore, Style, init

solved_cube = [
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