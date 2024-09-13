import sys
from random import randint
import pygame
from game import Game

pygame.init()

screen_width = 750
screen_height = 700
OFFSET = 50

GREY = (29, 29, 30)
YELLOW = (243, 216, 63)

BACKGROUND = pygame.image.load('Graphics/background.png')

font = pygame.font.Font("font/monogram.ttf", 40)

game = Game(screen_width, screen_height, OFFSET)

level_text_surface = font.render(f"LEVEL", False, YELLOW)

game_over_surface = font.render("GAME OVER", False, YELLOW)
score_text_surface = font.render("SCORE", False, YELLOW)
highscore_text_surface = font.render("HIGH-SCORE", False, YELLOW)

screen = pygame.display.set_mode((screen_width + OFFSET, screen_height + OFFSET * 2))
pygame.display.set_caption("Python Space Invaderz")

clock = pygame.time.Clock()

SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)

MYSTERY_SHIP = pygame.USEREVENT + 1
pygame.time.set_timer(MYSTERY_SHIP, randint(4000, 8000))
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SHOOT_LASER and game.run:
            game.alien_shoot_laser()

        if event.type == MYSTERY_SHIP and game.run:
            game.create_mystery_ship()
            pygame.time.set_timer(MYSTERY_SHIP, randint(4000, 8000))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_f] and not game.run:
            game.reset()
    # background draw
    screen.blit(BACKGROUND, (0, 0))

    # update spaceship group
    if game.run:
        game.spaceship_group.update()
        game.move_aliens()
        game.alien_lasers_group.update()
        game.mystery_ship_group.update()
        game.power_up_group.update()
        game.check_for_collisions()
        game.explosion_group.update()
        game.bullet_explosion.update()

    # Drawing

    pygame.draw.rect(screen, YELLOW, (10, 10, 780, 780), 2, 0, 60, 60, 60, 60)
    pygame.draw.line(screen, YELLOW, (25, 730), (775, 730), 3)

    # level and game over message UI
    if game.run:
        screen.blit(level_text_surface, (570, 740, 50, 50))
        level_surface = font.render(f"{game.level:02}", False, YELLOW)
        screen.blit(level_surface, (650, 740, 50, 50))
    else:
        screen.blit(game_over_surface, (570, 740, 50, 50))

    x = 50
    # lives UI
    for life in range(game.lives):
        screen.blit(game.spaceship_group.sprite.image, (x, 745))
        x += 50

    # score and highscore UI
    screen.blit(score_text_surface, (50, 15, 50, 50))
    score_surface = font.render(str(game.score).zfill(7), False, YELLOW)
    screen.blit(score_surface, (50, 40, 50, 50))

    screen.blit(highscore_text_surface, (600, 15, 50, 50))
    highscore_surface = font.render(str(game.highscore).zfill(7), False, YELLOW)
    screen.blit(highscore_surface, (645, 40, 50, 50))

    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)
    game.aliens_group.draw(screen)
    game.alien_lasers_group.draw(screen)
    game.mystery_ship_group.draw(screen)
    game.power_up_group.draw(screen)
    game.explosion_group.draw(screen)
    game.bullet_explosion.draw(screen)

    pygame.display.update()
    clock.tick(60)
