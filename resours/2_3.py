from pygame import *
from pygame.constants import *
from random import *

from all_colors import *
pygame.init()

size = (1200, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("новая игра")
BACKGROUND = (255,255,255)
screen.fill(BACKGROUND)
FPS = 60
width, height = 100, 100
x, y = 50, 50
speed = 5
color = RED



clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False





    keys = pygame.key.get_pressed()




    if keys[K_LEFT]:
        x -= speed
    if keys[K_RIGHT]:
        x += speed
    if keys[K_UP]:
        y -= speed
    if keys[K_DOWN]:
        y += speed

    if x < 0:
        x = 0
        color = choice(COLORS)
        continue
    if x > size[0] - width:
        x = size[0] - width
        color = choice(COLORS)
        continue

    if y < 0:
        y = 0
        color = choice(COLORS)
        continue
    if y > size[1] - height:
        y = size[1] - height
        color = choice(COLORS)
        continue




    screen.fill(BACKGROUND)
    pygame.draw.rect(screen,color,(x,y,width,height))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()