import pygame
from bullet import Bullet
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
        self.player_group = self.player1, self.player2
        self.startButton = Button(pygame.transform.scale(pygame.image.load("Media/StartknappSnanks.png"), (500, 250)), 950, 400, "", self.display_surface)
        self.end_screen_picture = pygame.transform.scale(pygame.image.load("Media/DetSlutSnanks.png"), (screen_width, screen_height))
        self.start_pressed = False
        self.intro_screen()

    def intro_screen(self):
        if self.start_pressed or self.startButton.check_for_input():
            self.main_game()
            self.start_pressed = True
        else:
            self.startButton.update()

    def collide(self):
        # Checks if bullets have collided with the other player but ignores collision otherwise
        for player in self.player_group:
            all_collisions = pygame.sprite.spritecollide(self.player2, self.player1.bullets, False)
            all_collisions += pygame.sprite.spritecollide(self.player1, self.player2.bullets, False)
            for bullet in all_collisions:
                if bullet.id != player.id:
                    player.hitpoints -= 1
                    bullet.kill()

    def draw_health_bars(self):
        # Draws health bar
        player1_pos = self.player1.position
        player2_pos = self.player2.position
        pygame.draw.rect(self.display_surface, "green", (player1_pos[0] - 10, player1_pos[1] - 10, 13*self.player1.hitpoints, 5))
        pygame.draw.rect(self.display_surface, "green", (player2_pos[0] - 10, player2_pos[1] - 10, 13*self.player2.hitpoints, 5))

    def main_game(self):
        if self.player1.hitpoints > 0 and self.player2.hitpoints > 0:
            self.run()
            self.draw_health_bars()
            self.collide()

        else:
            self.end_screen()

    def end_screen(self):
        self.display_surface.blit(self.end_screen_picture, (0, 0))

    def run(self):
        self.player1.run()
        self.player2.run()
