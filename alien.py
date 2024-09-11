import pygame
from random import choice


class Alien(pygame.sprite.Sprite):
    def __init__(self, alien_type, x, y):
        super().__init__()
        self.type = alien_type
        path = f"Graphics/alien_{alien_type}.png"
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, direction):
        self.rect.x += direction


class MysteryShip(pygame.sprite.Sprite):
    def __init__(self, screen_width, offset):
        super().__init__()
        self.screen_width = screen_width
        self.offset = offset
        self.image = pygame.image.load("Graphics/mystery.png")
        x = choice([self.offset / 2, self.screen_width + self.offset - self.image.get_width()])
        if x == self.offset / 2:
            self.speed = 3
        else:
            self.speed = -3
        self.rect = self.image.get_rect(topleft=(x, 90))

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > self.screen_width + self.offset / 2:
            self.kill()
        elif self.rect.left < self.offset / 2:
            self.kill()


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, power_type, screen_height, x_position):
        super().__init__()
        self.power_type = power_type
        path = f"Graphics/power_{power_type}.png"
        self.screen_height = screen_height
        self.x_position = x_position
        self.image = pygame.image.load(path)
        self.speed = 3
        self.rect = self.image.get_rect(topleft=(x_position, 90))

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.screen_height:
            self.kill()
