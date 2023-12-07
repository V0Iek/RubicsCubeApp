#!/usr/bin/env python3

import pygame as pg

from cube import RubicsCube
from Classes import Button
from playground import playground
import translate as tr


# Funkcje
def scramble():
    cube.scramble()
    cube.draw_cube(screen)

def newCube():
    cube.reset()
    cube.draw_cube(screen)

def plygrnd():
    global buttons
    buttons = playground(screen, cube)

    btn_back = Button(screen, 550, screen.get_height() * .85, 100, 50, "Back", (128, 128, 128), (0, 128, 128), back)

    buttons.append(btn_back)

def back():
    global buttons
    buttons = [btn_scramble, btn_solve, btn_playground, btn_exit]

    screen.fill(background_color)

def ext():
    global running
    running = False


# Zmienne
size = width, height = (1920, 1080)

background_color = (50, 50, 50)

cube = RubicsCube()


# Startowy kod
pg.init()
running = True

screen = pg.display.set_mode(size) # pg.RESIZABLE
pg.display.set_caption("Rubics Cube Lerner")
screen.fill(background_color)

btn_scramble = Button(screen, width * .05, height * .8, width / 5 * 2, 50, "Wymieszaj kostkę", (128, 128, 128), (0, 128, 128), scramble)
btn_solve = Button(screen, width / 2 + width * .05, height * .8, width / 5 * 2, 50, "Ułóż kostkę", (128, 128, 128), (0, 128, 128), newCube)
btn_playground = Button(screen, width * .05, height * .9, width / 5 * 2, 50, "Playground", (128, 128, 128), (0, 128, 128), plygrnd)
btn_exit = Button(screen, width / 2 + width * .05, height * .9, width / 5 * 2, 50, "Wyjście", (128, 128, 128), (0, 128, 128), ext)

buttons = [btn_scramble, btn_solve, btn_playground, btn_exit]


# Glowna petla
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # elif event.type == pg.VIDEORESIZE:
        #     if width > height:
        #         rect_size = int(height / 15)
        #     else:
        #         rect_size = int(width / 15)

        for button in buttons:
            button.handle_event(event)

    # Rysowanie przycisków
    for button in buttons:
        if button.rect.collidepoint(pg.mouse.get_pos()):
            button.draw(button.hover_color)
        else:
            button.draw(button.color)

    # cube.draw_cube(screen)
    cube.project_cube(screen)
    pg.display.flip()


# Zakonczenie
pg.quit()