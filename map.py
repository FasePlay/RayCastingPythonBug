from settings import *

text_map = [
    "111111111111",
    "100000000001",
    "101110000101",
    "100000001111",
    "111100001001",
    "100000001111",
    "100111000011",
    "111111111111"
]

world_map = set()

for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == '1':
            world_map.add((i * TILE, j * TILE))