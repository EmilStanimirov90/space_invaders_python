import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, position, speed, screen_height, laser_type):
        super().__init__()
        path = f"graphics/laser_{laser_type}.png"
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=position)
        self.speed = speed
        self.screen_height = screen_height

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y > self.screen_height + 15 or self.rect.y < 0:
            self.kill()
