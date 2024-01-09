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

text_map_3 = [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'W............X.......X......X.W',
    'W..XXX....XXXX.....X...XXXX...W',
    'WX...........X.....X....XXX...W',
    'W..XXX.............X..........W',
    'W....X.......X.....XXXX.....XXW',
    'W....X.....XXX...........X....W',
    'W..XXX.......X...X.....XXX....W',
    'W................XXXXXXX......W',
    'WX...XX..XX..X...X........XX..W',
    'W............X.......XX.......W',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'
]

text_map = text_map_3

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
