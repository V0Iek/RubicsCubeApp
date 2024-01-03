#!/usr/bin/env python3

import pygame as pg

from cube import RubicsCube
from classes import Button
from playground import playground
from timer import CubeTimer
import translate as tr


# Funkcje
def scramble():
    cube.scramble()

def newCube():
    cube.reset()

def plygrnd():
    screen.fill(background_color)

    global buttons
    buttons = playground(screen, cube)

    btn_back = Button(screen, width * .05, height * .95, width * .9, height / 21.6, "Back", (128, 128, 128), (0, 128, 128), back)

    buttons.append(btn_back)

def back():
    screen.fill(background_color)

    global handle_timer
    handle_timer = False

    global buttons
    buttons = [btn_scramble, btn_solve, btn_playground, btn_exit, btn_timer]

def timer():
    screen.fill(background_color)

    global handle_timer
    handle_timer = True

    global buttons
    buttons = []

    btn_back = Button(screen, width * .05, height * .95, width * .9, height / 21.6, "Back", (128, 128, 128), (0, 128, 128), back)

    buttons.append(btn_back)

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
handle_timer = False

screen = pg.display.set_mode(size) # pg.RESIZABLE
pg.display.set_caption("Rubics Cube Lerner")
screen.fill(background_color)

btn_scramble = Button(screen, width * .05, height * .8, width / 5 * 2, height / 21.6, "Wymieszaj kostkę", (128, 128, 128), (0, 128, 128), scramble)
btn_solve = Button(screen, width / 2 + width * .05, height * .8, width / 5 * 2, height / 21.6, "Ułóż kostkę", (128, 128, 128), (0, 128, 128), newCube)
btn_playground = Button(screen, width * .05, height * .85, width / 5 * 2, height / 21.6, "Playground", (128, 128, 128), (0, 128, 128), plygrnd)
btn_exit = Button(screen, width / 2 + width * .05, height * .85, width / 5 * 2, height / 21.6, "Wyjście", (128, 128, 128), (0, 128, 128), ext)
btn_timer = Button(screen, width * .05, height * .9, width / 5 * 2, height / 21.6, "Timer", (128, 128, 128), (0, 128, 128), timer)

buttons = [btn_scramble, btn_solve, btn_playground, btn_exit, btn_timer]

cube_timer = CubeTimer(screen)


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

        if handle_timer:
            key_pressed_time = 0
            target_duration = 5000
            
            cube_timer.show(screen)
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    key_pressed_time = pg.time.get_ticks()
                    cube_timer.ready(screen)

            keys = pg.key.get_pressed()

            if keys[pg.K_SPACE]:
                current_time = pg.time.get_ticks()
                elapsed_time = current_time - key_pressed_time

                if elapsed_time >= target_duration:
                    cube_timer.can_start = True
                    cube_timer.ready(screen)

            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    if cube_timer.can_start:
                        cube_timer.start(screen)
                    else:
                        cube_timer.reset(screen)

    # Rysowanie przycisków
    for button in buttons:
        if button.rect.collidepoint(pg.mouse.get_pos()):
            button.draw(button.hover_color)
        else:
            button.draw(button.color)

    cube.draw_cube(screen)
    # cube.project_cube(screen)
    pg.display.flip()


# Zakonczenie
pg.quit()