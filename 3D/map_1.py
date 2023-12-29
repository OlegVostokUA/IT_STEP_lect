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
    'W...XX.........W',
    'W...XX.........W',
    'W.........XX...W',
    'W........XXX...W',
    'W..............W',
    'W........XXXXXXW',
    'W..............W',
    'WXXX...........W',
    'W..............W',
    'WWWWWWWWWWWWWWWW'
]

text_map = text_map_2

world_map = set()
mini_map = set()

world_map = {}
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            if char == 'W':
                world_map[(i * TILE, j * TILE)] = '1'
            elif char == 'X':
                world_map[(i * TILE, j * TILE)] = '2'
