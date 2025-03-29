import math

import pygame
pygame.init()

size = (1200, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("новая игра")
BACKGROUND = (255,255,255)
screen.fill(BACKGROUND)
FPS = 60
clock = pygame.time.Clock()

BUTTON_COLOR = (0,191,255)
HOVER_COLOR = (0,140,255)
CLICK_COLOR = (0,50,255)

BUTTON_RADIUS = 50
BUTTON_CENTER = [size[0]//2, size[1]/2]

hovering = False
clicking = False

def distance(p1,p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            if (distance(event.pos,BUTTON_CENTER)< BUTTON_RADIUS):
                hovering = True
            else:
                hovering = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (event.button ==3 and distance(event.pos,BUTTON_CENTER)< BUTTON_RADIUS):
                clicking = True
        elif event.type == pygame.MOUSEBUTTONUP:
            clicking = False
    screen.fill(BACKGROUND)
    if clicking:
        button_color = CLICK_COLOR
    elif hovering:
        button_color = HOVER_COLOR
    else:
        button_color = BUTTON_COLOR
    pygame.draw.circle(screen, button_color,BUTTON_CENTER,BUTTON_RADIUS)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()