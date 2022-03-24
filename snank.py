import pygame


class Snank:
    def __init__(self, screen, pos, id):
        super(Snank, self).__init__()
        self.display_surface = screen
        self.position = pos
        self.id = id
        self.speed = 3
        self.direction = pygame.math.Vector2(0, 0)
        self.image = pygame.Surface((20, 20))
        self.image.fill("green")
        self.rect = self.image.get_rect(center=self.position)


    def get_input(self):
        keys = pygame.key.get_pressed()
        if self.id == 0:
            if(keys[pygame.K_w]):
                self.direction = 0, -self.speed
            if(keys[pygame.K_a]):
                self.direction = -self.speed, 0
            if(keys[pygame.K_s]):
                self.direction = 0, self.speed
            if(keys[pygame.K_d]):
                self.direction = self.speed, 0
            if(keys[pygame.K_SPACE]):
                pass # Spawn bullet going direction

        if self.id == 1:
            if(keys[pygame.K_UP]):
                self.direction = 0, -self.speed
            if(keys[pygame.K_LEFT]):
                self.direction = -self.speed, 0
            if(keys[pygame.K_DOWN]):
                self.direction = 0, self.speed
            if(keys[pygame.K_RIGHT]):
                self.direction = self.speed, 0
            if(keys[pygame.K_b]):
                pass # Spawn bullet going direction
        self.position += self.direction

    def run(self):

        self.get_input()
        self.display_surface.blit(self.image, self.position)
