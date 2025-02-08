from all_colors import *
import pygame as pg
pg.init()
size = (1280, 720)
screen = pg.display.set_mode(size)
pg.display.set_caption("Примитивы")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
line_color = RED
line_width = 5
start_pos = (0, size[1]//2)
end_pos = (size[0], size[1]//2)
FPS = 60
clock = pg.time.Clock()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill(BACKGROUND)
    pg.draw.line(screen, line_color, start_pos, end_pos, line_width)
    pg.draw.rect(screen, ORANGE,(50,50,100,100))
    pg.draw.rect(screen, YELLOW, (100, 100, 100, 100))
    pg.draw.rect(screen, GREEN, (150, 150, 100, 100))
    pg.draw.rect(screen, ORANGE, (250, 50, 100, 100),5)
    pg.draw.rect(screen, YELLOW, (300, 100, 100, 100), 5)
    pg.draw.rect(screen, GREEN, (350, 150, 100, 100),5)
    pg.draw.rect(screen, ORANGE, (450, 50, 100, 100),border_radius=10)
    pg.draw.rect(screen, YELLOW, (500, 100, 100, 100), border_radius=10)
    pg.draw.rect(screen, GREEN, (550, 150, 100, 100), border_radius=10)
    pg.draw.ellipse(screen, ORANGE, (50, 450, 100,100))
    pg.draw.ellipse(screen, YELLOW, (100, 500, 100, 100))
    pg.draw.ellipse(screen, GREEN, (150, 550, 100, 100))
    pg.draw.ellipse(screen, ORANGE, (250, 450, 100, 100),5)
    pg.draw.ellipse(screen, YELLOW, (300, 500, 100, 100), 5)
    pg.draw.ellipse(screen, GREEN, (350, 550, 100, 100),5)
    pg.draw.polygon(screen,ORANGE,((750,250),(800,300),(850,250)))
    pg.draw.polygon(screen,YELLOW,((750,350),(800,400),(850,350)))
    pg.draw.polygon(screen, GREEN,((750,450),(800,500),(850,450)))



    pg.display.flip()
    clock.tick(FPS)
pg.quit()