import pygame as  pg

win_res = (1280,720)
game_title = " Magic Game "
clock = pg.time.Clock()
is_fs = False

#win_icon = pg.image.load()
#pygame.display.set_icon(winIcon)

pg.init()
main_win = pg.display.set_mode(win_res, pg.RESIZABLE)