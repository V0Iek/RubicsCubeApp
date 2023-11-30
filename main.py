#!/usr/bin/env python3

import pygame

from cube import RubicsCube
from playground import playground


# Klasy
# Klasa reprezentujaca przycisk
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action

    def draw(self, color):
        pygame.draw.rect(screen, color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, (255, 255, 255))
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
                    int(p * rect_size * 1.1 + rect_size * 3.3 * x),
                    int(l * rect_size * 1.1 + rect_size * 3.3 * y),
                    rect_size,
                    rect_size
                )
            )

def draw_cube():
    draw_side(0, 1, 0)
    draw_side(4, 0, 1)
    draw_side(1, 1, 1)
    draw_side(2, 2, 1)
    draw_side(3, 3, 1)
    draw_side(5, 1, 2)
    pygame.display.update()

def scramble():
    cube.scramble()
    draw_cube()

def newCube():
    cube.reset()

def playgnd():
    print("Playground")

def ext():
    running = False


# Zmienne
size = width, height = (800, 800)
rect_size = int(width / 15)

cube = RubicsCube()

btn_scramble = Button(width / 4 - width / 8, height * .8, 200, 50, "Wymieszaj kostkę", (128, 128, 128), (0, 128, 128), scramble)
btn_solve = Button(width / 2 + width / 8, height * .8, 200, 50, "Ułóż kostkę", (128, 128, 128), (0, 128, 128), newCube)
btn_playground = Button(width / 4 - width / 8, height * .9, 200, 50, "Playground", (128, 128, 128), (0, 128, 128), playgnd)
btn_exit = Button(width / 2 + width / 8, height * .9, 200, 50, "Wyjście", (128, 128, 128), (0, 128, 128), ext)

buttons = [btn_scramble, btn_solve, btn_playground, btn_exit]


# Startowy kod
pygame.init()
running = True

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rubics Cube Lerner")

draw_cube()


# Glowna petla
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        for button in buttons:
            button.handle_event(event)

    # Rysowanie przycisków
    for button in buttons:
        if button.rect.collidepoint(pygame.mouse.get_pos()):
            button.draw(button.hover_color)
        else:
            button.draw(button.color)

    pygame.display.flip()


# Zakonczenie
pygame.quit()