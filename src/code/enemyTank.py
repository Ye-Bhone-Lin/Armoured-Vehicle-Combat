import random
import pygame


class opponetTank:
    def __init__(self, x, y, screen, health, image, speed):
        icon = pygame.transform.scale(pygame.image.load(image), (50, 50))
        self.x = x
        self.y = y
        self.health = health
        self.screen = screen
        self.icon = icon
        self.speed = speed

    def horizontalMovement(self):
        if random.randint(0, 1) == 0:
            self.x += 40
        elif random.randint(0, 1) == 1:
            self.x -= 40

    def move(self):
        self.y += self.speed

    def display(self):
        self.screen.blit(self.icon, (self.x, self.y))

    def healthRecuded(self):
        self.health -= 10

    def healthBar(self, screen, x, y):
        font = pygame.font.Font('robosapien.ttf', 25)
        if self.health == 0:
            health = font.render('ELIMINATED', True, (0, 255, 0))
        else:
            health = font.render('Health : ' + str(self.health), True, (255, 0, 0))
        screen.blit(health, (x, y))
