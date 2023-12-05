import pygame as pg

class Button:
    def __init__(self, screen, x, y, width, height, text, color, hover_color, action):
        self.screen = screen
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action

    def draw(self, color):
        pg.draw.rect(self.screen, color, self.rect)
        font = pg.font.Font(None, 36)
        text = font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.rect.center)
        self.screen.blit(text, text_rect)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()