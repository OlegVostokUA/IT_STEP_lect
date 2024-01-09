import pygame
from settings import *
from ray_casting import ray_casting
from map_1 import mini_map

class Drawing:
    def __init__(self, window, m_map_scr):
        self.window = window
        self.m_map_scr = m_map_scr
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.texture = {'1': pygame.image.load('textures/wals.jpg').convert(),
                         '2': pygame.image.load('textures/wals2.jpg').convert(),
                         'S': pygame.image.load('textures/sky.png').convert()
                         }

    def background(self, angle):
        sky_offset = -15 * math.degrees(angle) % WIDTH
        self.window.blit(self.texture['S'], (sky_offset, 0))
        self.window.blit(self.texture['S'], (sky_offset - WIDTH, 0))
        self.window.blit(self.texture['S'], (sky_offset + WIDTH, 0))
        pygame.draw.rect(self.window, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.window.blit(object, object_pos)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, DARKORANGE)
        self.window.blit(render, FPS_POS)

    def mini_map(self, player):
        self.m_map_scr.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.line(self.m_map_scr, YELLOW, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                 map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.m_map_scr, RED, (int(map_x), int(map_y)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.m_map_scr, DARKBROWN, (x, y, MAP_TILE, MAP_TILE))
        self.window.blit(self.m_map_scr, MAP_POS)
