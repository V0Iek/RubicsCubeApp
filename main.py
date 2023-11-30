#!/usr/bin/env python3

from os import system, name
from colorama import Fore, Style, init

import pygame

from cube import RubicsCube
from playground import playground


# Zmienne
size = width, height = (800, 800)
rect_size = int(width / 15)

cube = RubicsCube()


# Klasy
# Klasa reprezentująca przycisk
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()


# Funkcje
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


# Startowy kod
pygame.init()
running = True

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rubics Cube Lerner")

draw_cube()


# Główna pętla
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# Zakończenie
pygame.quit()