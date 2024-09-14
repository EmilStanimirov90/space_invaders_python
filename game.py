import pygame
from pygame.examples.aliens import Explosion

from laser import Laser
from spaceship import Spaceship
from obstacle import Obstacle
from obstacle import grid
from alien import Alien, MysteryShip, PowerUp, Explosion, BulletExplosion
from random import choice


class Game:
    def __init__(self, screen_width, screen_height, offset):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.offset = offset
        self.spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship_group.add(Spaceship(self.screen_width, self.screen_height + 20, self.offset))
        self.obstacles = self.create_obstacles()
        self.aliens_group = pygame.sprite.Group()
        self.create_aliens()
        self.aliens_direction = 1
        self.alien_speed = 1
        self.alien_lasers_group = pygame.sprite.Group()
        self.mystery_ship_group = pygame.sprite.GroupSingle()
        self.power_up_group = pygame.sprite.GroupSingle()
        self.explosion_group = pygame.sprite.Group()
        self.bullet_explosion_group = pygame.sprite.GroupSingle()
        self.run = True
        self.lives = 3
        self.score = 0
        self.highscore = 0
        self.aliens_killed = 0
        self.level = 1
        self.power_ups_list = [1, 2, 3, 4, 6]
        self.load_highscore()
        self.explosion_sound = pygame.mixer.Sound("Sounds/force-field-impact-15.wav")
        self.shield_sound = pygame.mixer.Sound("Sounds/large-underwater-explosion-190270.mp3")
        self.power_up_sound = pygame.mixer.Sound("Sounds/power-on.wav")
        pygame.mixer.music.load("Sounds/Shadows Of Tomorrow.mp3")
        pygame.mixer.music.play(-1)

    def create_obstacles(self):
        obstacle_width = len(grid[0]) * 3
        gap = (self.screen_width + self.offset - (4 * obstacle_width)) / 5
        obstacles = []
        for i in range(4):
            offset_x = (i + 1) * gap + i * obstacle_width
            obstacle = Obstacle(offset_x, self.screen_height - 100)
            obstacles.append(obstacle)
        return obstacles

    def create_aliens(self):
        for row in range(5):
            for column in range(11):
                cell_size = 55
                x = 75 + column * cell_size
                y = 110 + row * cell_size
                if row == 0:
                    alien_type = 3
                elif row in (1, 2):
                    alien_type = 2
                else:
                    alien_type = 1

                alien = Alien(alien_type, x + self.offset / 2, y)
                self.aliens_group.add(alien)

    def move_aliens(self):

        alien_sprites = self.aliens_group.sprites()

        for alien in alien_sprites:
            if alien.rect.right >= self.screen_width + self.offset / 2:

                self.aliens_direction = -1

                self.alien_move_down(1 + self.level / 2)

            elif alien.rect.left <= self.offset / 2:
                self.aliens_direction = 1

                self.alien_move_down(1 + self.level / 2)
        self.aliens_group.update(self.aliens_direction)

    def alien_move_down(self, distance):
        if self.aliens_group:
            for alien in self.aliens_group.sprites():
                alien.rect.y += distance

    def alien_shoot_laser(self):
        if self.aliens_group.sprites():
            random_alien = choice(self.aliens_group.sprites())
            laser_sprite = Laser(random_alien.rect.center[0], random_alien.rect.center[1], 0, -6, self.screen_height, 4,
                                 1, 0)
            self.alien_lasers_group.add(laser_sprite)

    def create_mystery_ship(self):
        self.mystery_ship_group.add(MysteryShip(self.screen_width, self.offset))

    def create_power_up(self):

        if self.lives > 9 and 2 in self.power_ups_list:
            self.power_ups_list.remove(2)
        else:
            if 2 not in self.power_ups_list:
                self.power_ups_list.append(2)

        if self.spaceship_group.sprite.laser_strength >= 3 and 3 in self.power_ups_list:
            self.power_ups_list.remove(3)
        else:
            if 3 not in self.power_ups_list:
                self.power_ups_list.append(3)

        random_power = choice(self.power_ups_list)
        self.power_up_group.add(
            PowerUp(random_power, self.screen_height, self.mystery_ship_group.sprite.rect.center[0]))

    def create_explosion(self, x, y, scale):
        self.explosion_group.add(Explosion(x, y, scale))

    def create_bullet_explosion(self, x, y, scale):
        self.bullet_explosion_group.add(BulletExplosion(x, y, scale))

    def check_for_collisions(self):

        # spaceship lasers
        if self.spaceship_group.sprite.lasers_group:
            for laser_sprite in self.spaceship_group.sprite.lasers_group:

                aliens_hit = pygame.sprite.spritecollide(laser_sprite, self.aliens_group, True)
                if aliens_hit:
                    self.explosion_sound.play()
                    for alien in aliens_hit:
                        self.score += alien.type * 10 * self.level
                        self.check_for_highscore()
                        self.check_level_up()
                        self.create_explosion(laser_sprite.rect[0], laser_sprite.rect[1], 3)

                        self.create_bullet_explosion(laser_sprite.rect[0], laser_sprite.rect[1], 1)
                        laser_sprite.kill()

                        self.aliens_killed += 1

                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        self.create_bullet_explosion(laser_sprite.rect.midtop[0], laser_sprite.rect.midtop[1], 1)
                        laser_sprite.kill()

                # mystery ship
                if pygame.sprite.spritecollide(laser_sprite, self.mystery_ship_group, False):
                    self.explosion_sound.play()
                    self.score += 50 * self.level
                    self.check_for_highscore()
                    self.create_power_up()
                    self.create_bullet_explosion(laser_sprite.rect[0], laser_sprite.rect[1], 1)
                    laser_sprite.kill()

                    self.create_explosion(self.mystery_ship_group.sprite.rect[0],
                                          self.mystery_ship_group.sprite.rect[1], 3)
                    self.mystery_ship_group.sprite.kill()

        # Get power UP
        if self.power_up_group:
            if pygame.sprite.spritecollide(self.power_up_group.sprite, self.spaceship_group, False):
                self.power_up_sound.play()

                if self.power_up_group.sprite.power_type == 1:
                    self.spaceship_group.sprite.increase_laser_speed()

                elif self.power_up_group.sprite.power_type == 2:
                    self.lives += 1

                elif self.power_up_group.sprite.power_type == 3:
                    self.spaceship_group.sprite.increase_laser_strength()

                elif self.power_up_group.sprite.power_type == 4:
                    self.spaceship_group.sprite.increase_laser_count()
                    self.power_ups_list.remove(4)
                    self.power_ups_list.append(5)

                elif self.power_up_group.sprite.power_type == 5:
                    self.power_ups_list.remove(5)
                    self.power_ups_list.append(7)
                    self.spaceship_group.sprite.increase_laser_count()

                elif self.power_up_group.sprite.power_type == 6:
                    self.spaceship_group.sprite.increase_fire_speed()

                elif self.power_up_group.sprite.power_type == 7:
                    self.power_ups_list.remove(7)
                    self.power_ups_list.append(8)
                    self.spaceship_group.sprite.increase_laser_count()

                elif self.power_up_group.sprite.power_type == 8:
                    self.power_ups_list.remove(8)
                    self.spaceship_group.sprite.increase_laser_count()

                self.power_up_group.sprite.kill()

        # ALien lasers
        if self.alien_lasers_group:
            for laser_sprite in self.alien_lasers_group:
                if pygame.sprite.spritecollide(laser_sprite, self.spaceship_group, False):
                    self.shield_sound.play()
                    self.create_explosion(laser_sprite.rect[0], laser_sprite.rect[1], 2)
                    laser_sprite.kill()
                    self.lives -= 1
                    self.spaceship_group.sprite.reset_laser_count()
                    self.power_ups_list = [1, 2, 3, 4, 6]
                    if self.lives == 0:
                        self.game_over()
                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        self.create_explosion(laser_sprite.rect[0], laser_sprite.rect[1], 1)
                        laser_sprite.kill()

        # ships collisions

        if self.aliens_group:
            for alien in self.aliens_group:
                for obstacle in self.obstacles:
                    pygame.sprite.spritecollide(alien, obstacle.blocks_group, True)
                if pygame.sprite.spritecollide(alien, self.spaceship_group, False):
                    self.game_over()
                if alien.rect.midbottom[1] >= self.screen_width:
                    self.game_over()

    def game_over(self):
        self.run = False

    def reset(self):
        self.run = True
        self.lives = 3
        self.spaceship_group.sprite.reset()
        self.aliens_group.empty()
        self.alien_lasers_group.empty()
        self.mystery_ship_group.empty()
        self.power_up_group.empty()
        self.explosion_group.empty()
        self.bullet_explosion_group.empty()
        self.obstacles = self.create_obstacles()
        self.score = 0
        self.level = 1
        self.power_ups_list = [1, 2, 3, 4, 6]
        self.aliens_killed = 0

        self.create_aliens()

    def check_for_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score

            with open("highscore.txt", "w") as file:
                file.write(str(self.highscore))

    def load_highscore(self):
        try:
            with open("highscore.txt", "r") as file:
                self.highscore = int(file.read())
        except FileNotFoundError:
            self.highscore = 0

    def level_up(self):
        self.level += 1
        self.aliens_group.empty()
        self.aliens_killed = 0
        self.create_aliens()

    def check_level_up(self):
        if not self.aliens_group.sprites():
            self.level_up()
