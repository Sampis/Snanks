import pygame

import game
from snank import Snank
from settings import *
from button import Button


class Game:
    def __init__(self, screen):
        self.display_surface = screen

        self.snank = pygame.sprite.GroupSingle()
        self.menu_font = pygame.font.SysFont("IMPACT", 60)
        self.player1 = Snank(screen, (screen_width/4-20, screen_height/2), 0)
        self.player2 = Snank(screen, (screen_width/4*3, screen_height/2), 1)
        self.startButton = Button(pygame.transform.scale(pygame.image.load("Media/StartknappSnanks.png"), (500, 250)), 950, 400, "", self.display_surface)
        self.start_pressed = False
        self.intro_screen()

    def intro_screen(self):
        if self.start_pressed or self.startButton.check_for_input():
            self.main_game()
            self.start_pressed = True
        else:
            self.startButton.update()

    def main_game(self):
        self.run()

    def end_screen(self):
        pass

    def run(self):
        self.player1.run()
        self.player2.run()
