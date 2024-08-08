import pygame
from planet import Planet

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True

pl1 = Planet(50, 50, 1, 50, (0, 0, 255))

while run:

    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        pl1.move(-1, 0)
    elif keys[pygame.K_RIGHT]:
        pl1.move(1, 0)
    elif keys[pygame.K_UP]:
        pl1.move(0, -1)
    elif keys[pygame.K_DOWN]:
        pl1.move(0, 1)

    win.fill((0, 0, 0))

    pygame.draw.circle(win, pl1.color, (pl1.x, pl1.y), pl1.mass)
    pygame.display.update()
    

pygame.quit()