
import pygame


class Snank:
    def __init__(self, screen, pos):
        super(Snank, self).__init__()
        self.display_surface = screen
        self.position = pos
        self.image = pygame.Surface((100, 100))
        self.image.fill("green")
        self.rect = self.image.get_rect(center=self.position)

    def get_input(self):
        print(self)

    def run(self):

        self.get_input()
        self.display_surface.blit(self.image, self.position)
