#!/usr/bin/env python3

from os import system, name
from colorama import Fore, Style, init

import pygame

from cube import RubicsCube
from playground import playground


size = width, height = (800, 800)
rect_size = int(width / 15)

cube = RubicsCube()

pygame.init()
running = True

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rubics Cube Lerner")

def draw_side(index, x, y):
    for l in range(3):
        for p in range(3):
            pygame.draw.rect(
                screen,
                cube.state[index][l][p],
                (
                    int(p * rect_size * 1.1) + rect_size * 3.3 * x,
                    int(l * rect_size * 1.1) + rect_size * 3.3 * y,
                    rect_size,
                    rect_size
                )
            )

def draw_cube():
    draw_side(0, 0, 0)
    draw_side(1, 0, 1)
    draw_side(2, 1, 1)
    draw_side(3, 2, 1)
    draw_side(4, 3, 1)
    draw_side(5, 0, 2)
    pygame.display.update()

draw_cube()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()