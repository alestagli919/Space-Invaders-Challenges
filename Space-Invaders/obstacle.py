import pygame
import random


class Obstacle:
    def __init__(self):
        self.size = random.randint(20, 70)
        self.x = random.randint(0, 800 - self.size)
        self.y = -self.size
        self.speed = 4
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def move(self):
        self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
