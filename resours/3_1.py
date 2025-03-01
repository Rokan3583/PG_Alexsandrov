import pygame
from all_colors import *
pygame.init()

size = (1200, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("новая игра")
<<<<<<< HEAD
BACKGROUND = (255,255,255)
screen.fill(BACKGROUND)

COLORS = [BLACK, WHITE, RED, GREEN, YELLOW, CYAN, MAGENTA, GRAY,
          ORANGE, PINK, BROWN, PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, COLD]

rect1 = pygame.Rect(100,100,200,150)
rect2 = pygame.Rect(250,150,200,150)

rect3 = pygame.Rect(500,100,200,150)
rect4 = pygame.Rect(600,300,200,150)
width = 5

def collizenion(rect,other_rect):
    if rect.colliderect(other_rect):
        pygame.draw.rect(screen,RED,rect,width)
        pygame.draw.rect(screen, RED,other_rect, width)
    else:
        pygame.draw.rect(screen,BLUE,rect,width)
        pygame.draw.rect(screen, BLUE,other_rect, width)


collizenion(rect1,rect2)
collizenion(rect3,rect4)

=======
BACKGROUND = (50,255,50)
screen.fill(BACKGROUND)
rect1 = pygame.Rect(100,100, 200, 150)
rect2 = pygame.Rect(250,150, 200, 150)
rect3 = pygame.Rect(500,100, 200, 150)
rect4 = pygame.Rect(600,300, 200, 150)
width = 5
def collision(rect,other_rect):
    if rect.colliderect(other_rect):
        pygame.draw.rect(screen, RED, rect, width)
        pygame.draw.rect(screen, RED, other_rect, width)
    else:
        pygame.draw.rect(screen, BLUE, rect, width)
        pygame.draw.rect(screen, BLUE, other_rect, width)
collision(rect1, rect2)
collision(rect3, rect4)
>>>>>>> 19b00346b9c0cf976fcd3fb27728f657b1eb4c33
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

<<<<<<< HEAD
=======

>>>>>>> 19b00346b9c0cf976fcd3fb27728f657b1eb4c33
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()