import sys

import pygame

screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    snake_head_sprite = pygame.image.load("Media/SnankHuvud.png")
    snake_body_sprite = pygame.image.load("Media/SnankKropp.png")
    screen.fill('black')
    screen.blit(snake_head_sprite, (500, 500))
    clock.tick(60)
    pygame.display.flip()
