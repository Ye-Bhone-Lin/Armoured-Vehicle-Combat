import pygame


class Character:
    def __init__(self, x, y, screen, image):
        icon = pygame.transform.scale(pygame.image.load(image), (50,50))
        self.x = x
        self.y = y
        self.screen = screen
        self.icon = icon

    def moveRight(self):
        self.x += 3

    def moveLeft(self):
        self.x -= 3

    def display(self):
        self.screen.blit(self.icon, (self.x, self.y))

