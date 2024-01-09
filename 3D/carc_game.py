import pygame
from settings import *
from player import Player
import math
from map_1 import *
from sprite_objects import *
from ray_casting import ray_casting
from drawing import Drawing

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
m_map_scr = pygame.Surface((WIDTH // MAP_SCALE + 115, HEIGHT // MAP_SCALE))

sprites = Sprites()
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
    drawing.background(player.angle)
    walls = ray_casting(player, drawing.texture)
    drawing.world(walls + [obj.object_locate(player, walls) for obj in sprites.list_of_objects])
    drawing.fps(clock)
    # drawing.m_map_draw(player)

    ###
    pygame.display.flip()
    clock.tick(

    )
    
pygame.quit()
