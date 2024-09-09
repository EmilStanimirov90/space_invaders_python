import pygame
from laser import Laser


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load("graphics/spaceship.png")
        self.rect = self.image.get_rect(midbottom=(self.screen_width / 2, self.screen_height))
        self.speed = 6
        self.lasers_group = pygame.sprite.Group()
        self.laser_ready_fire = True
        self.laser_time = 0
        self.laser_delay = 300

    def get_user_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_f] and self.laser_ready_fire:
            self.laser_ready_fire = False
            speed = 5
            laser = Laser(self.rect.center, speed, self.screen_height)
            self.lasers_group.add(laser)
            self.laser_time = pygame.time.get_ticks()

    def update(self):
        self.get_user_input()
        self.constrain_movement()
        self.lasers_group.update()
        self.recharge_laser()

    def constrain_movement(self):
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.left < 0:
            self.rect.left = 0

    def recharge_laser(self):
        if not self.laser_ready_fire:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_delay:
                self.laser_ready_fire = True

    def reset(self):
        self.rect = self.image.get_rect(midbottom =(self.screen_width/2, self.screen_height))
        self.lasers_group.empty()