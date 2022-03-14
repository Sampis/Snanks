import sys
import pygame
from settings import *
from game import Game

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill("black")
    game.intro_screen()
    clock.tick(60)
    pygame.display.flip()
