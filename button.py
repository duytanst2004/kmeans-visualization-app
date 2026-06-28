import pygame
from config import BLACK, WHITE


class TextButton:
    def __init__(self, text, x, y, width, height):
        self.text   = text
        self.x      = x
        self.y      = y
        self.width  = width
        self.height = height

    def is_hovered(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return self.x < mouse_x < self.x + self.width and \
               self.y < mouse_y < self.y + self.height

    def draw(self, screen, font):
        text_surface = font.render(self.text, True, WHITE)
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))
        screen.blit(text_surface, (self.x + self.width / 10, self.y + self.height / 10))
