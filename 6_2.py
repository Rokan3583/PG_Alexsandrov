import pygame
import math
pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("новая игра")
BACKGROUND = (255,255,255)
screen.fill(BACKGROUND)
FPS = 60

BUTTON_COLOR = (0,191,255)
HOVER_COLOR = (0,140,255)
CLICK_COLOR = (0,50,255)

BUTTON_RADIUS = 50
BUTTON_CENTER = [size[0]//2,size[1]//2]

hovering =False
clicking = False

# def distance(p1,p2):
#     return  math.sqrt((p2[0] - p1[0])
#                       **2 + (p2[1]- p1[1]) **2)

button_rect = pygame.Rect(BUTTON_CENTER[0] - BUTTON_RADIUS,
                          BUTTON_CENTER[1] - BUTTON_RADIUS,
                          BUTTON_RADIUS *2,
                          BUTTON_RADIUS)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEMOTION:
            # if (distance(event.pos, BUTTON_CENTER)
            #         < BUTTON_RADIUS):
            if button_rect.collidepoint(event.pos):
                hovering = True
            else:
                hovering = False

            if clicking:
                BUTTON_CENTER[0] = event.pos[0]
                BUTTON_CENTER[1] = event.pos[1]

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # if (event.button == 3 and distance(event.pos,
            #         BUTTON_CENTER)
            #         <BUTTON_RADIUS):
            if event.button == 3 and button_rect.collidepoint(event.pos):
                clicking =True
        elif event.type == pygame.MOUSEBUTTONUP:
            clicking = False


    screen.fill(BACKGROUND)

    if clicking:
        buttom_color = CLICK_COLOR
    elif hovering:
        buttom_color = HOVER_COLOR
    else:
        buttom_color = BUTTON_COLOR

    pygame.draw.circle(screen, buttom_color,BUTTON_CENTER,
                       BUTTON_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()