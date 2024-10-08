import pygame
from laser import Laser


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, offset):
        super().__init__()
        self.offset = offset
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load("graphics/spaceship.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=((self.screen_width + self.offset) / 2, self.screen_height))
        self.ship_move_speed = 6
        self.lasers_group = pygame.sprite.Group()
        self.laser_ready_fire = True
        self.laser_time = 0
        self.laser_delay = 300
        self.laser_speed = 5
        self.laser_strength = 1
        self.laser_count = 1
        self.laser_type = 1
        self.laser_offset = 0

        self.laser_sound = pygame.mixer.Sound("Sounds/plasma-shot-01.flac")

    def get_user_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.ship_move_speed

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.ship_move_speed

        if keys[pygame.K_f] and self.laser_ready_fire:
            self.laser_ready_fire = False

            if self.laser_count == 1:

                for i in range(self.laser_strength):
                    laser = Laser(self.rect.center[0], self.rect.center[1] - 20, self.laser_offset - self.laser_strength, self.laser_speed, self.screen_height, self.laser_type, self.laser_strength , 0)
                    self.lasers_group.add(laser)

            elif self.laser_count == 2:

                for i in range(self.laser_strength):
                    laser2 = Laser(self.rect.center[0] + 18, self.rect.center[1] - 20, self.laser_offset - self.laser_strength, self.laser_speed, self.screen_height, self.laser_type, self.laser_strength ,0)
                    self.lasers_group.add(laser2)
                    laser3 = Laser(self.rect.center[0] - 18, self.rect.center[1] - 20, self.laser_offset - self.laser_strength, self.laser_speed, self.screen_height, self.laser_type, self.laser_strength,0)
                    self.lasers_group.add(laser3)

            elif self.laser_count == 3:

                for i in range(self.laser_strength):
                    laser = Laser(self.rect.center[0], self.rect.center[1] - 22, self.laser_offset - self.laser_strength, self.laser_speed, self.screen_height,
                                  self.laser_type, self.laser_strength,0)
                    self.lasers_group.add(laser)
                    laser2 = Laser(self.rect.center[0] + 18, self.rect.center[1] - 20, self.laser_offset - self.laser_strength, self.laser_speed,
                                   self.screen_height, self.laser_type, self.laser_strength,0)
                    self.lasers_group.add(laser2)
                    laser3 = Laser(self.rect.center[0] - 18, self.rect.center[1] - 20, self.laser_offset - self.laser_strength, self.laser_speed,
                                   self.screen_height, self.laser_type, self.laser_strength,0)
                    self.lasers_group.add(laser3)

            elif self.laser_count == 4:
                for i in range(self.laser_strength):
                    laser = Laser(self.rect.center[0], self.rect.center[1] - 22, self.laser_offset - self.laser_strength, self.laser_speed, self.screen_height,
                                  self.laser_type, self.laser_strength,0)
                    self.lasers_group.add(laser)
                    laser2 = Laser(self.rect.center[0] + 20, self.rect.center[1] - 20, self.laser_offset - self.laser_strength, self.laser_speed,
                                   self.screen_height, self.laser_type, self.laser_strength,0)
                    self.lasers_group.add(laser2)
                    laser3 = Laser(self.rect.center[0] - 20, self.rect.center[1] - 20, self.laser_offset - self.laser_strength, self.laser_speed,
                                   self.screen_height, self.laser_type, self.laser_strength,0)
                    self.lasers_group.add(laser3)
                    laser4 = Laser(self.rect.center[0] + 20, self.rect.center[1] - 20,
                                   self.laser_offset - self.laser_strength, self.laser_speed,
                                   self.screen_height, self.laser_type, self.laser_strength, -1)
                    self.lasers_group.add(laser4)
                    laser5 = Laser(self.rect.center[0] - 20, self.rect.center[1] - 20,
                                   self.laser_offset - self.laser_strength, self.laser_speed,
                                   self.screen_height, self.laser_type, self.laser_strength, 1)
                    self.lasers_group.add(laser5)

            elif self.laser_count == 5:
                for i in range(self.laser_strength):
                    laser = Laser(self.rect.center[0], self.rect.center[1] - 22,
                                  self.laser_offset - self.laser_strength, self.laser_speed, self.screen_height,
                                  self.laser_type, self.laser_strength, 0)
                    self.lasers_group.add(laser)
                    laser2 = Laser(self.rect.center[0] + 20, self.rect.center[1] - 20,
                                   self.laser_offset - self.laser_strength, self.laser_speed,
                                   self.screen_height, self.laser_type, self.laser_strength, 0)
                    self.lasers_group.add(laser2)
                    laser3 = Laser(self.rect.center[0] - 20, self.rect.center[1] - 20,
                                   self.laser_offset - self.laser_strength, self.laser_speed,
                                   self.screen_height, self.laser_type, self.laser_strength, 0)
                    self.lasers_group.add(laser3)
                    laser4 = Laser(self.rect.center[0] + 20, self.rect.center[1] - 20,
                                   self.laser_offset - self.laser_strength, self.laser_speed,
                                   self.screen_height, self.laser_type, self.laser_strength, -1)
                    self.lasers_group.add(laser4)
                    laser5 = Laser(self.rect.center[0] - 20, self.rect.center[1] - 20,
                                   self.laser_offset - self.laser_strength, self.laser_speed,
                                   self.screen_height, self.laser_type, self.laser_strength, 1)
                    self.lasers_group.add(laser5)
                    laser6 = Laser(self.rect.center[0] + 22, self.rect.center[1] - 20,
                                   self.laser_offset - self.laser_strength, self.laser_speed,
                                   self.screen_height, self.laser_type, self.laser_strength, -2)
                    self.lasers_group.add(laser6)
                    laser7 = Laser(self.rect.center[0] - 22, self.rect.center[1] - 20,
                                   self.laser_offset - self.laser_strength, self.laser_speed,
                                   self.screen_height, self.laser_type, self.laser_strength, 2)
                    self.lasers_group.add(laser7)

            self.laser_time = pygame.time.get_ticks()
            self.laser_sound.play()

    def update(self):
        self.get_user_input()
        self.constrain_movement()
        self.lasers_group.update()
        self.recharge_laser()

    def constrain_movement(self):
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.left < self.offset:
            self.rect.left = self.offset

    def recharge_laser(self):
        if not self.laser_ready_fire:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_delay:
                self.laser_ready_fire = True

    def reset(self):
        self.rect = self.image.get_rect(midbottom=((self.screen_width + self.offset) / 2, self.screen_height))
        self.lasers_group.empty()
        self.laser_ready_fire = True
        self.laser_time = 0
        self.laser_delay = 300
        self.laser_speed = 5
        self.laser_strength = 1
        self.laser_count = 1
        self.laser_type = 1

    def increase_fire_speed(self):
        if self.laser_delay >= 40:
            self.laser_delay -= 30
        if self.laser_delay < 40:
            self.laser_delay = 4

    def increase_laser_speed(self):
        if self.laser_speed <= 18:
            self.laser_speed += 2
        if self.laser_speed > 18:
            self.laser_speed = 18

    def increase_laser_count(self):
        self.laser_count += 1

        if self.laser_count > 5:
            self.laser_count = 5

    def reset_laser_count(self):
        self.laser_count = 1

    def increase_laser_strength(self):

        self.laser_strength += 1
        if self.laser_strength == 3:
            self.laser_strength = 3

    def change_laser_color(self):
        pass

    def get_laser_strength(self):
        return self.laser_strength
