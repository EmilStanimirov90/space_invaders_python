import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y, offset, speed, screen_height, laser_type, laser_strength, diagonal_move):
        super().__init__()
        path = f"graphics/laser_{laser_type}.png"
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x + offset, y))
        self.laser_strength = laser_strength
        self.diagonal_move = diagonal_move

        if self.laser_strength == 1:
            self.image = pygame.transform.scale(self.image, (4, 15))
        elif self.laser_strength == 2:
            self.image = pygame.transform.scale(self.image, (6, 23))
        elif self.laser_strength == 3:
            self.image = pygame.transform.scale(self.image, (9, 35))

        self.speed = speed
        self.screen_height = screen_height

    def update(self):
        self.rect.y -= self.speed
        self.rect.x -= self.diagonal_move

        if self.rect.y > self.screen_height + 15 or self.rect.y < 0:
            self.kill()
