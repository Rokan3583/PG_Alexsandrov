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
rect_size = 200
speed = 5
x = 0
y = 0
color = [RED, BLACK]
# rect1 = pygame.Rect(x, y, rect_size, rect_size)
# rect1.center = (screen.get_width()//2, screen.get_height()//2)
# pygame.draw.rect(screen,BLACK,rect1)
#
# rect2 = pygame.Rect(x, y, rect_size//2, rect_size//2)
# rect2.center = (screen.get_width()//2, screen.get_height()//2)
# pygame.draw.rect(screen,RED,rect2)
for i in range(2):
    rect1 = pygame.Rect(x, y, rect_size//i, rect_size//i)
    rect1.center = (screen.get_width() // 2, screen.get_height() // 2)
    pygame.draw.rect(screen, color(i), rect1)


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #
    # keys = pygame.key.get_pressed()
    #
    #
    #
    #
    # if keys[K_LEFT]:
    #     x -= speed
    # if keys[K_RIGHT]:
    #     x += speed
    # if keys[K_UP]:
    #     y -= speed
    # if keys[K_DOWN]:
    #     y += speed
    #
    # if x < 0:
    #     x = 0
    #     color = choice(COLORS)
    #     continue
    # if x > size[0] - width:
    #     x = size[0] - width
    #     color = choice(COLORS)
    #     continue
    #
    # if y < 0:
    #     y = 0
    #     color = choice(COLORS)
    #     continue
    # if y > size[1] - height:
    #     y = size[1] - height
    #     color = choice(COLORS)
    #     continue
    #





    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()