import pygame
from entity import * 
from mainmenu import *
from pygame.locals import *
from spritesheet import * 



class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1280, 720
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.title = pygame.display.set_caption("Magic Game")
        self.font_name = 'Assets\\fonts\\chubbyChoo.ttf'
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.currentMenu = self.main_menu

    def loop(self):
        self.tiles = Spritesheet('Assets/Images/global.png', 16, 16, 10, 10)
        global resize
        resize = False
        curr_scale = 1
        screen_space = pygame.sprite.Group()
        sun = Entity(100,100,"Assets/Images/global.png")
        screen_space.add(sun)
        while self.playing:
            keys = pygame.key.get_pressed()
            self.checkEvents()
            if self.BACK_KEY:
                self.playing= False

            if keys[pygame.K_w]:
                sun.y -= 1
            if keys[pygame.K_s]:
                sun.y += 1
            if keys[pygame.K_d]:
                sun.x += 1
            if keys[pygame.K_a]:
                sun.x -= 1

            #sun.x, sun.y = pygame.mouse.get_pos()
            
            self.display.fill((0,100,0))
            self.window.blit(self.display, (0,0))
            #screen_space.draw(self.window)
            #screen_space.update()

            #self.window.blit(self.tiles.getTile(1,2), (72, 72))
 
            pygame.display.update()


            self.resetKeys()



    def checkEvents(self):
        global resize
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.currentMenu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.START_KEY = True
                if event.key == pygame.K_LEFT:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    
    def resetKeys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def drawText(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)