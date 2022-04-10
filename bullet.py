import pygame
from settings import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, rot, dir, speed):
        super(Bullet, self).__init__()

        self.direction = dir
        self.speed = speed

        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Media/bullet.png"), (10, 5)), rot)
        # Fixa hastighets problemet
        self.rect = self.image.get_rect(center=(pos[0]+10+(dir[0]*(speed*5)), pos[1]+10+(dir[1]*(speed*5))))

    def move_bullet(self):
        self.rect.x += self.direction[0] * self.speed * 1
        self.rect.y += self.direction[1] * self.speed * 1

    def update(self):
        self.move_bullet()
        if (self.rect.x >= screen_width + 200 or self.rect.x <= - 200 or self.rect.y >= screen_height + 200 or self.rect.y <= - 200):
            self.kill()
