from game import Game

g = Game()

while g.running:
    g.currentMenu.displayMenu()
    g.loop()