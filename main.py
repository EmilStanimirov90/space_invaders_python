import sys
import pygame
from game import Game

pygame.init()

screen_width = 750
screen_height = 700

GREY = (29, 29, 30)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Python Space Invaderz")

clock = pygame.time.Clock()

game = Game(screen_width,screen_height)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # update spaceship group
    game.spaceship_group.update()

    # Drawing
    screen.fill(GREY)
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)

    pygame.display.update()
    clock.tick(60)
