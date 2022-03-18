import pygame
from settings import *


class Game:
    def __init__(self, screen):
        self.display_surface = screen

        self.snank = pygame.sprite.GroupSingle()
        self.menu_font = pygame.font.SysFont("IMPACT", 100)
        self.intro_screen()

    def intro_screen(self):
        pygame.draw.rect(self.display_surface, (255, 255, 255), (screen_width/2-200, screen_height/2+100, 400, 100), 4)
        pygame.draw.rect(self.display_surface, (255, 255, 255), (screen_width/2-200, screen_height/2+225, 400, 100), 4)
        pygame.draw.rect(self.display_surface, (255, 255, 255), (screen_width/2-200, screen_height/2+350, 400, 100), 4)
        start_text = self.menu_font.render(f"Start", 1, ("white"))
        start_text = pygame.transform.scale(start_text, (400, 125))
        self.display_surface.blit(start_text, (screen_width/2-200, screen_height/2+87.5))
        pygame.draw.circle(self.display_surface, ("red"), (screen_width/2, screen_height/2), 1)



    def run(self):
        pass
