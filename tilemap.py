import pygame
from pygame.locals import *
from random import randrange

mapFiles = []
mapTiles = []

class Map(pygame.sprite.Sprite):
    def __init__(self, tile_track, y, x, rot):
        pygame.sprite.Sprite.__init__(self)
        self.image = mapFiles[tile_track]
        self.rect = self.image.get_rect()

        if rot !=0:
            self.image = pygame.transform.rotate(self.image, rot * 90)

        self.x = x
        self.y = y

    def update(self, cam_x, cam_y):
        self.rect.topleft = self.x - cam_x, self.y - cam_y