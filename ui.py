# import os
import pygame
import pygame.freetype


class Label:
    def __init__(self, font, font_size, text, colour, win):
        self.font = font
        self.font_size = font_size
        self.text = text
        self.colour = colour
        self.win = win
        lbl_font = pygame.freetype.Font(font, font_size)
    def render_label(self, x, y):
        self.x = x
        self.y = y 
        self.lbl_surface = self.font.render(self.text, antialias=False, color=self.colour)
        self.win.blit(self.lbl_surface, dest=(self.x,self.y))
    def enable_aa(self, enable):
        self.enable = enable
        self.lbl_surface = self.font.render(self.text, antialias=self.enable, color=self.colour)



