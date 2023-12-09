from settings import *


text_map = [
    'WWWWWWWWWWWWWWW',
    'W.............W',
    'W.............W',
    'W.............W',
    'W.............W',
    'W.............W',
    'W.............W',
    'WWWWWWWWWWWWWWW'
]

world_map = set()

for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))