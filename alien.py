import pygame
from random import choice


class Alien(pygame.sprite.Sprite):
    def __init__(self, alien_type, x, y):
        super().__init__()
        self.type = alien_type
        path = f"Graphics/alien_{alien_type}{alien_type}.png"
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
        self.rect = self.image.get_rect(topleft=(x, 80))

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


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        super().__init__()
        self.images = []
        for num in range(1, 8):
            path = f"Graphics/exp_{num}.png"
            img = pygame.image.load(path)
            if scale == 1:
                img = pygame.transform.scale(img, (35, 35))
            elif scale == 2:
                img = pygame.transform.scale(img, (58, 58))
            elif scale == 3:
                img = pygame.transform.scale(img, (100, 100))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.counter = 0

    def update(self):
        explosion_speed = 3
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()


class BulletExplosion(pygame.sprite.Sprite):

    def __init__(self, x, y, scale):
        super().__init__()

        path = f"Graphics/bullet explosion.png"
        self.image = pygame.image.load(path)
        if scale == 1:
            self.image = pygame.transform.scale(self.image, (35, 35))
        elif scale == 2:
            self.image = pygame.transform.scale(self.image, (58, 58))
        elif scale == 3:
            self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect(center=(x, y))
        self.counter = 0

    def update(self):
        explosion_speed = 5
        self.counter += 1

        if self.counter >= explosion_speed:
            self.counter = 0
            self.kill()
