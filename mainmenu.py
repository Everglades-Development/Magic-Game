import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 200

    def drawPointer(self):
        self.game.drawText('>', 50, self.cursor_rect.x, self.cursor_rect.y)

    def blitScreen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.resetKeys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Start'
        self.startx, self.starty = self.mid_w, self.mid_h - 55
        self.optionsx, self.optionsy = self.mid_w, self.mid_h
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 55
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def displayMenu(self):
        self.run_display = True
        while self.run_display:
            self.game.checkEvents()
            self.checkInput()
            self.game.display.fill(self.game.BLACK)
            self.game.drawText('Magic Game Menu', 75, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 275)
            self.game.drawText('Start Game', 50, self.startx, self.starty)
            self.game.drawText('Options', 50, self.optionsx, self.optionsy)
            self.game.drawText('Credits', 50, self.creditsx, self.creditsy)
            self.drawPointer()
            self.blitScreen()


    def movePointer(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

    def checkInput(self):
        self.movePointer()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.currentMenu = self.game.options
            elif self.state == 'Credits':
                self.game.currentMenu = self.game.credits
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h 
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 55
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def displayMenu(self):
        self.run_display = True
        while self.run_display:
            self.game.checkEvents()
            self.checkInput()
            self.game.display.fill((0, 0, 0))
            self.game.drawText('Options', 75, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 200)
            self.game.drawText('Volume', 50, self.volx, self.voly)
            self.game.drawText('Controls', 50, self.controlsx, self.controlsy)
            self.drawPointer()
            self.blitScreen()

    def checkInput(self):
        if self.game.BACK_KEY:
            self.game.currentMenu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def displayMenu(self):
        self.run_display = True
        while self.run_display:
            self.game.checkEvents()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.currentMenu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.drawText('Credits', 75, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 200)
            self.game.drawText('Everglades Development', 65, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 55)
            self.game.drawText('Patrick Taylor - @patoriko', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 15 )
            self.game.drawText('Wesley Maguire - @wesmags', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 70)
            self.blitScreen()