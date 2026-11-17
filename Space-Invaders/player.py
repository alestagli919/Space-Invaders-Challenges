import pygame


class Player:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.color = color
        self.speed = 5
        self.lives = 3
        self.invulnerable_time = 0

    def move(self, keys, up, down, left, right):
        if self.lives == 0:
            return

        if keys[up]:
            self.rect.y -= self.speed
        if keys[down]:
            self.rect.y += self.speed
        if keys[left]:
            self.rect.x -= self.speed
        if keys[right]:
            self.rect.x += self.speed

        self.rect.clamp_ip(pygame.Rect(0, 0, 800, 600))

    def change_speed(self, amount):
        self.speed += amount
        self.speed = max(2, min(12, self.speed))

    def hit(self):
        if self.lives > 0 and self.invulnerable_time == 0:
            self.lives -= 1
            self.invulnerable_time = 2000

    def update(self, elapsed_time):
        if self.invulnerable_time > 0:
            self.invulnerable_time -= elapsed_time
            self.invulnerable_time = max(0, self.invulnerable_time)

    def draw(self, screen):
        if self.lives == 0:
            return
        if self.invulnerable_time > 0:
            if (self.invulnerable_time // 150) % 2 == 0:
                return
        pygame.draw.rect(screen, self.color, self.rect)
