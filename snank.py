import pygame
from settings import *
from bullet import Bullet
import time


class Snank:
    def __init__(self, screen, pos, id):
        super(Snank, self).__init__()
        self.display_surface = screen
        self.position = pygame.math.Vector2(pos[0], pos[1])
        self.id = id
        self.speed = 5
        self.rotation = 0
        self.direction = pygame.math.Vector2(0, 0)
        self.image = pygame.transform.scale(pygame.image.load("Media/SnankKropp.png"), (20, 20))
        self.rect = self.image.get_rect(center=self.position)
        self.bullets = pygame.sprite.Group()
        self.font = pygame.font.SysFont("IMPACT", 20)
        self.can_shoot = True
        self.bullet_spawn_speed = 1
        self.hitpoints = 3

    def detect_collision(self):
        if self.position[0] > screen_width-20:
            self.position[0] = screen_width-20
            self.direction = 0, 0
        elif self.position[0] < 0:
            self.position[0] = 0
            self.direction = 0, 0
        if self.position[1] > screen_height-20:
            self.position[1] = screen_height-20
            self.direction = 0, 0
        elif self.position[1] < 0:
            self.position[1] = 0
            self.direction = 0, 0
        if pygame.sprite.spritecollide(self, self.bullets, True):
            self.hitpoints -= 1
            if self.hitpoints == 0:
                pass

    def get_input(self):
        keys = pygame.key.get_pressed()
        start = time.time()
        time_left = int(start + self.bullet_spawn_speed - time.time())
        if self.id == 0:
            if keys[pygame.K_w]:
                self.direction = 0, -1
                self.rotation = 90
            elif keys[pygame.K_a] :
                self.direction = -1, 0
                self.rotation = 180
            elif keys[pygame.K_s] :
                self.direction = 0, 1
                self.rotation = -90
            elif keys[pygame.K_d]:
                self.direction = 1, 0
                self.rotation = 0
            if keys[pygame.K_SPACE] and self.direction != (0, 0) and self.can_shoot:
                # Spawn bullet going direction
                bullet = Bullet(self.position, self.rotation, self.direction, self.speed)
                self.bullets.add(bullet)
                self.can_shoot = False
            if time_left <= 0:
                self.can_shoot = True

        if self.id == 1:
            if keys[pygame.K_UP]:
                self.direction = 0, -1
                self.rotation = 90
            elif(keys[pygame.K_LEFT]):
                self.direction = -1, 0
                self.rotation = 180
            elif(keys[pygame.K_DOWN]):
                self.direction = 0, 1
                self.rotation = -90
            elif(keys[pygame.K_RIGHT]):
                self.direction = 1, 0
                self.rotation = 0
            if(keys[pygame.K_b] and self.direction != (0, 0) and self.can_shoot):
                # Spawn bullet going direction
                bullet = Bullet(self.position, self.rotation, self.direction, self.speed)
                self.bullets.add(bullet)
                self.can_shoot = False
            elif(not keys[pygame.K_b]):
                self.can_shoot = True

        self.position[0] += self.direction[0] * self.speed
        self.position[1] += self.direction[1] * self.speed
        self.rect = self.image.get_rect(center=self.position)
        self.detect_collision()

    def run(self):
        self.get_input()
        self.bullets.draw(self.display_surface)
        self.display_surface.blit(self.image, self.position)
        self.bullets.update()
