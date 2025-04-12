def remove_point(mouse_pos):
    for point in points:
        if ((point[0] - mouse_pos[0]) ** 2 + (point[1] - mouse_pos[1]) ** 2 <= RADIUS**2):
            points.remove(point)
            break

def hightlight_closent_point(mouse_pos):
    closent_point = None
    closent_distanse = float('inf')
    for point in points:
        distanse = ((point[0] - mouse_pos[0]) ** 2 +
                    (point[1] - mouse_pos[1]) ** 2)**0.5
        if distanse <= RADIUS**2 and distanse < closent_distanse:
            closent_point = point
            closent_distanse = distanse
    if closent_point is not None:
        pygame.draw.circle(screen,HIGHTLIGHT_COLOR,closent_point, RADIUS)

import pygame

from all_colors import *

pygame.init()

size = (1200, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("новая игра")
BACKGROUND = (0,0,0)
screen.fill(BACKGROUND)

points = []
LINE_COLOR = (255,255,255)
PREVUEW_COLOR =(192,192,192)
HIGHTLIGHT_COLOR = (255,0,0)
RADIUS = 5
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                points.append(event.pos)
            elif event.button == 3:
                remove_point(event.pos)

    screen.fill(BACKGROUND)
    for i in range(len(points)-1):

        start_point = points[i]
        end_point = points[i+1]
        pygame.draw.line(screen,LINE_COLOR,start_point,end_point,3)
    if len(points)>1:
        last_point = points[-1]
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.aaline(screen, PREVUEW_COLOR, last_point, mouse_pos, 3)
    hightlight_closent_point(pygame.mouse.get_pos())
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()