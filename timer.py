import pygame as pg

class CubeTimer:
    def __init__(self, screen):
        self.font = pg.font.Font(None, 128)

        self.timer_text = self.font.render("00:00.00", True, (255, 255, 255))
        self.timer_pos = self.timer_text.get_rect()
        self.timer_pos.center = (screen.get_width() / 2, screen.get_height() * .8)

        self.can_start = False
        self.started = False


    def show(self, screen):
        screen.blit(self.timer_text, self.timer_pos)


    def ready(self, screen):
        if self.can_start == False:
            self.timer_text = self.font.render("00:00.00", True, (255, 50, 50))

        else:
            self.timer_text = self.font.render("00:00.00", True, (50, 255, 50))

        self.timer_pos = self.timer_text.get_rect()
        self.timer_pos.center = (screen.get_width() / 2, screen.get_height() * .8)

        self.show(screen)


    def start(self, screen):
        self.time = 0
        self.started = True
        while self.started:
            self.time += 1

            self.timer_text = self.font.render(str(self.time), True, (255, 255, 255))
            self.timer_pos = self.timer_text.get_rect()
            self.timer_pos.center = (screen.get_width() / 2, screen.get_height() * .8)

            self.show(screen)


    def stop(self, screen):
        self.started = False


    def reset(self, screen):
        self.timer_text = self.font.render("00:00.00", True, (255, 255, 255))
        self.timer_pos = self.timer_text.get_rect()
        self.timer_pos.center = (screen.get_width() / 2, screen.get_height() * .8)

        self.show(screen)