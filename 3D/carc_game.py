import pygame
from settings import *
from player import Player
import math
from map_1 import *
from ray_casting import ray_casting
from drawing import Drawing

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
m_map_scr = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(window, m_map_scr)

    
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    player.movement()
    window.fill(BLACK)
    ###
    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)
    drawing.m_map_draw(player)

    ###
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()
