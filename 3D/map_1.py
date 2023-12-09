from settings import *


text_map_1 = [
    'WWWWWWWWWWWWWWWW',
    'W..............W',
    'W..............W',
    'W..............W',
    'W..............W',
    'W..............W',
    'W..............W',
    'W..............W',
    'W..............W',
    'W..............W',
    'W..............W',
    'WWWWWWWWWWWWWWWW'
]
text_map_2 = [
    'WWWWWWWWWWWWWWWW',
    'W..............W',
    'W...WW.........W',
    'W...WW.........W',
    'W.........WW...W',
    'W........WWW...W',
    'W..............W',
    'W........WWWWWWW',
    'W..............W',
    'WWWW...........W',
    'W..............W',
    'WWWWWWWWWWWWWWWW'
]

text_map = text_map_2

world_map = set()
mini_map = set()

for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))
            mini_map.add((i * MAP_TILE, j * MAP_TILE))

