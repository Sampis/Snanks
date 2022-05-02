import sys
import pygame
from settings import *
from game import Game

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game(screen)
keys = pygame.key.get_pressed()

while not keys[pygame.K_ESCAPE]:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    screen.fill("black")
    game.intro_screen()
    clock.tick(60)
    pygame.display.flip()
