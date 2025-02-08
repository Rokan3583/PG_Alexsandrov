import pygame as pg
import  random
from all_colors import *
pg.init()

# pg.mixer.init()
# pg.mixer.music.load("resours/La La Land")
# pg.mixer.music.play(-1)



size = (0, 0)
screen = pg.display.set_mode(size,pg.FULLSCREEN)
pg.display.set_caption("Дискотека")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
FPS = 60
clock = pg.time.Clock()
running = True
timer = 0


COLORS = [BLACK,WHITE,RED,BLUE,GREEN,YELLOW,CYAN,MAGENTA,GRAY,
          ORANGE,PINK,BROWN,PURPLE,LIME,NAVY,OlIVE,MAROON,TEAL,SILVER,GOLD]


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(random.choice(COLORS))
    pg.display.flip()
    pg.time.delay(random.randint(200,200))

pg.quit()