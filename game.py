import pygame

import game
from snank import Snank
from settings import *


class Game:
    def __init__(self, screen):
        self.display_surface = screen

        self.snank = pygame.sprite.GroupSingle()
        self.menu_font = pygame.font.SysFont("IMPACT", 60)
        self.intro_screen()
        self.player1 = Snank(screen, (screen_width/4-20, screen_height/2), 0)
        self.player2 = Snank(screen, (screen_width/4*3, screen_height/2), 1)

    def intro_screen(self):
        self.main_game()

    def main_game(self):
        #self.run()
        pass

    def end_screen(self):
        pass

    def run(self):
        self.player1.run()
        self.player2.run()
