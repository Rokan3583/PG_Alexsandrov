
import pygame

pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Рисование линий")
BACKGROUND = (0, 0, 0)
COLORS = (192, 192, 192)
LINE_COLOR = (255, 255, 255)
RED = (255, 0, 0)
RADIUS = 5
FPS = 60


lines = [[]]
current_line_index = 0
drawing = False

clock = pygame.time.Clock()
running = True


def get_closest_point(mouse_pos):
    closest_point = None
    closest_distance = float('inf')
    # Проверяем все точки во всех линиях
    for line in lines:
        for point in line:
            distance = ((point[0] - mouse_pos[0]) ** 2 +
                        (point[1] - mouse_pos[1]) ** 2) ** 0.5
            if distance <= RADIUS and distance < closest_distance:
                closest_point = point
                closest_distance = distance
    return closest_point


def remove_point(mouse_pos):
    for line in lines:
        for point in line:
            if ((point[0] - mouse_pos[0]) ** 2 +
                    (point[1] - mouse_pos[1]) ** 2 <= RADIUS ** 2):
                line.remove(point)
                return True
    return False


while running:
    mouse_pos = pygame.mouse.get_pos()
    closest_point = get_closest_point(mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if closest_point:
                    lines[current_line_index].append(closest_point)
                else:
                    lines[current_line_index].append(mouse_pos)
                drawing = True

            elif event.button == 3:
                if closest_point:
                    remove_point(closest_point)
                lines.append([])
                current_line_index = len(lines) - 1
                drawing = False

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False

        elif event.type == pygame.MOUSEMOTION and drawing:
            lines[current_line_index].append(mouse_pos)

    screen.fill(BACKGROUND)

    for line in lines:
        if len(line) > 1:
            pygame.draw.lines(screen, LINE_COLOR, False, line, 3)
    if lines[current_line_index] and not drawing:
        last_point = lines[current_line_index][-1]
        pygame.draw.aaline(screen, COLORS, last_point, mouse_pos, 3)
    if closest_point:
        pygame.draw.circle(screen, RED, closest_point, RADIUS, 1)


def remove_point(mouse_pos):
    for point in points:
        if ((point[0] - mouse_pos[0]) ** 2 + (point[1] - mouse_pos[1]) ** 2 <= RADIUS**2):
            points.remove(point)
            break

def get_closent_point(mouse_pos):
    closent_point = None
    closent_distanse = float('inf')
    for point in points:
        distanse = ((point[0] - mouse_pos[0]) ** 2 +
                    (point[1] - mouse_pos[1]) ** 2)**0.5
        if distanse <= RADIUS**2 and distanse < closent_distanse:
            closent_point = point
            closent_distanse = distanse
    return closent_point

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
    mouse_pos = pygame.mouse.get_pos()
    closent_point = get_closent_point(mouse_pos)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if closent_point:
                if event.button == 3:
                    remove_point(closent_point)
                elif event.button == 1:
                    points.append(closent_point)
                    print(points)
            elif event.button == 1:
                points.append(mouse_pos)


    screen.fill(BACKGROUND)
    for i in range(len(points)-1):
        pygame.draw.line(screen,LINE_COLOR,points[i],points[i+1],5)
    if len(points)>0:
        pygame.draw.aaline(screen, PREVUEW_COLOR, points[-1], mouse_pos, 3)
    if closent_point:
        pygame.draw.circle(screen, HIGHTLIGHT_COLOR,closent_point,RADIUS,1)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()