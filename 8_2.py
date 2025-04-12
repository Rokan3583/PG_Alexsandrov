import pygame

from all_colors import WHITE

pygame.init()

size = (1200, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("новая игра")
BACKGROUND = (0,0,0)
screen.fill(BACKGROUND)

points = []
LINE_COLOR = (255,255,255)
PREVUEW_COLOR =(192,192,192)
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            points.append(event.pos)
    screen.fill(BACKGROUND)
    for i in range(len(points)-1):

        start_point = points[i]
        end_point = points[i+1]
        pygame.draw.line(screen,LINE_COLOR,start_point,end_point,3)
    if len(points)>1:
        last_point = points[-1]
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.aaline(screen, PREVUEW_COLOR, last_point, mouse_pos, 3)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()