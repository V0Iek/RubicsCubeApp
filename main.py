#!/usr/bin/env python3

import pygame as pg

from cube import RubicsCube
import translate as tr


# Klasy
# Klasa reprezentujaca przycisk
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action

    def draw(self, color):
        pg.draw.rect(screen, color, self.rect)
        font = pg.font.Font(None, 36)
        text = font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()


# Funkcje
def scramble():
    cube.scramble()
    cube.draw_cube(screen)

def newCube():
    cube.reset()
    cube.draw_cube(screen)

def playground():
    btn_u = Button(10, height * .8, 50, 50, "U", (128, 128, 128), (0, 128, 128), cube.U)
    btn_up = Button(70, height * .8, 50, 50, "U'", (128, 128, 128), (0, 128, 128), cube.Up)
    btn_e = Button(130, height * .8, 50, 50, "E", (128, 128, 128), (0, 128, 128), cube.E)
    btn_ep = Button(190, height * .8, 50, 50, "E'", (128, 128, 128), (0, 128, 128), cube.Ep)
    btn_d = Button(250, height * .8, 50, 50, "D", (128, 128, 128), (0, 128, 128), cube.D)
    btn_dp = Button(310, height * .8, 50, 50, "D'", (128, 128, 128), (0, 128, 128), cube.Dp)
    btn_l = Button(370, height * .8, 50, 50, "L", (128, 128, 128), (0, 128, 128), cube.L)
    btn_lp = Button(430, height * .8, 50, 50, "L'", (128, 128, 128), (0, 128, 128), cube.Lp)
    btn_m = Button(490, height * .8, 50, 50, "M", (128, 128, 128), (0, 128, 128), cube.M)
    btn_mp = Button(10, height * .9, 50, 50, "M'", (128, 128, 128), (0, 128, 128), cube.Mp)
    btn_r = Button(70, height * .9, 50, 50, "R", (128, 128, 128), (0, 128, 128), cube.R)
    btn_rp = Button(130, height * .9, 50, 50, "R'", (128, 128, 128), (0, 128, 128), cube.Rp)
    btn_f = Button(190, height * .9, 50, 50, "F", (128, 128, 128), (0, 128, 128), cube.F)
    btn_fp = Button(250, height * .9, 50, 50, "F'", (128, 128, 128), (0, 128, 128), cube.Fp)
    btn_s = Button(310, height * .9, 50, 50, "S", (128, 128, 128), (0, 128, 128), cube.S)
    btn_sp = Button(370, height * .9, 50, 50, "S'", (128, 128, 128), (0, 128, 128), cube.Sp)
    btn_b = Button(430, height * .9, 50, 50, "B", (128, 128, 128), (0, 128, 128), cube.B)
    btn_bp = Button(490, height * .9, 50, 50, "B'", (128, 128, 128), (0, 128, 128), cube.Bp)
    btn_back = Button(550, height * .85, 100, 50, "Back", (128, 128, 128), (0, 128, 128), back)

    global buttons
    buttons = [btn_u, btn_up, btn_e, btn_ep, btn_d, btn_dp, btn_l, btn_lp, btn_m, btn_mp, btn_r, btn_rp, btn_f, btn_fp, btn_s, btn_sp, btn_b, btn_bp, btn_back]

    screen.fill(background_color)
    cube.draw_cube(screen)

    pg.display.update()

def back():
    global buttons
    buttons = [btn_scramble, btn_solve, btn_playground, btn_exit]

    screen.fill(background_color)
    cube.draw_cube(screen)

    pg.display.update()

def ext():
    global running
    running = False


# Zmienne
size = width, height = (1920, 1080)

background_color = (50, 50, 50)

cube = RubicsCube()

btn_scramble = Button(width * .05, height * .8, width / 5 * 2, 50, "Wymieszaj kostkę", (128, 128, 128), (0, 128, 128), scramble)
btn_solve = Button(width / 2 + width * .05, height * .8, width / 5 * 2, 50, "Ułóż kostkę", (128, 128, 128), (0, 128, 128), newCube)
btn_playground = Button(width * .05, height * .9, width / 5 * 2, 50, "Playground", (128, 128, 128), (0, 128, 128), playground)
btn_exit = Button(width / 2 + width * .05, height * .9, width / 5 * 2, 50, "Wyjście", (128, 128, 128), (0, 128, 128), ext)

buttons = [btn_scramble, btn_solve, btn_playground, btn_exit]


# Startowy kod
pg.init()
running = True

screen = pg.display.set_mode(size) # pg.RESIZABLE
pg.display.set_caption("Rubics Cube Lerner")
screen.fill(background_color)

cube.draw_cube(screen)


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

    cube.draw_cube(screen)
    pg.display.flip()


# Zakonczenie
pg.quit()