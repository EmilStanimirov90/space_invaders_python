import pygame


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, x, y, max_hp):
        super().__init__()
        self.hp_bar_length = 38

        self.max_hp = max_hp
        self.current_hp = self.max_hp

        self.hp_ratio = self.current_hp / self.max_hp
        self.image = pygame.image.load("Graphics/hp_bar.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.hp_bar_length, 2))
        self.rect = self.image.get_rect(topleft=(x, y - 7))
        self.is_visible = True

    #     grey = (138, 0, 0)
    #     green = (38, 252, 0)

    def take_damage(self, amount):
        self.is_visible = True

        if self.current_hp > 0:
            self.current_hp -= amount
        if self.current_hp <= 0:
            self.current_hp = 0

    def update(self, direction):

        self.rect.x += direction
        self.image = pygame.transform.scale(self.image, (self.hp_bar_length * self.hp_ratio, 2))

        if not self.is_visible:
            self.image.set_alpha(0)
        else:
            self.image.set_alpha(255)
