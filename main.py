import sys

import pygame

pygame.init()

screen = pygame.display.set_mode(1200, 600)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill('black')

    clock.tick(60)
    pygame.display.flip()