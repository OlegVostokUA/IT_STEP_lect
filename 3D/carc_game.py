import pygame
from settings import *
from player import Player
import math

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

    
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    player.movement()
    window.fill(BLACK)
    ###
    pygame.draw.circle(window, RED, player.pos, 12)
    pygame.draw.line(window, GREEN, player_pos, (player.x + WIDTH * math.cos(player.angle),
                                                 player.y + WIDTH * math.sin(player.angle)))
    ###
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()
