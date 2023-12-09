import pygame
from settings import *
from ray_casting import ray_casting
from map_1 import mini_map

class Drawing:
    def __init__(self, window, m_map_scr):
        self.window = window
        self.m_map_scr = m_map_scr
        self.font = pygame.font.SysFont('Arial', 36, bold=True)

    def background(self):
        pygame.draw.rect(self.window, SKYBLUE, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.window, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, player_pos, player_angle):
        ray_casting(self.window, player_pos, player_angle)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.window.blit(render, (WIDTH - 65, 5))

    def m_map_draw(self, player):
        self.m_map_scr.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE

        pygame.draw.line(self.m_map_scr, YELLOW, (map_x,map_y), (map_x + 12 * math.cos(player.angle),
                                                 map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.m_map_scr, RED, (int(map_x), int(map_y)), 5)
        for x,y in mini_map: # world_map_2
            pygame.draw.rect(self.m_map_scr, GREEN, (x, y, MAP_TILE, MAP_TILE))
        self.window.blit(self.m_map_scr, MAP_POS)
