
import pygame


class Snank(pygame.sprite.Sprite):
    def __init__(self, screen, pos):
        super(Snank, self).__init__()
        self.display_surface = screen
        self.position = pos
        self.image = pygame.Surface((400, 100))
        self.image.fill("green")
        self.rect = self.image.get_rect(center=self.position)

    def run(self):
        self.display_surface.blit(self.image, self.position)