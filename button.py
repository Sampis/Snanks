import pygame

# Credit till Noel för han typ trolla fram det här från internet.
# Dock jag tvung fix för han inte
# Också jag hade mer planer med detta men fick slut på tid


class Button:
    def __init__(self, image, x_pos, y_pos, text_input, screen):
        self.font = pygame.font.SysFont("cambria", 50)
        self.display_surface = screen
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def check_for_input(self):
        mousepos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        # Checks if mouse position is within button position
        if mousepos[0] in range(self.rect.left, self.rect.right) and mousepos[1] in range(self.rect.top, self.rect.bottom):
            if mouse[0]:
                self.display_surface.fill("black")
                return True
            else:
                pass
        else:
            pass

    def change_color(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, "green")
        else:
            self.text = self.font.render(self.text_input, True, "white")

    def update(self):
        self.display_surface.blit(self.image, self.rect)
        self.display_surface.blit(self.text, self.text_rect)
        self.check_for_input()
