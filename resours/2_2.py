import pygame
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= 5
                if y < 0:
                    y = 0
            elif event.key == pygame.K_DOWN:
                y += 5
                if y + height > size[1]:
                    y = size[1]-height
            elif event.key == pygame.K_LEFT:
                x -= 5
                if x < 0:
                    x = 0
            elif event.key == pygame.K_RIGHT:
                x += 5
                if x + width > size[0]:
                    x = size[0]-width
            else:
                print(f"нажата клавиша {event.key}")




    screen.fill(BACKGROUND)
    pygame.draw.rect(screen,color,(x,y,width,height))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()