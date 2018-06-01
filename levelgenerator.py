# Level generator for castle dungeons

import roomGenerator
import numpy as np
import random

# Find if a room can be placed and where.
#
# INPUT: same as find_room() but with a candidate room
# OUTPUT: -1 is room cannot be placed
#         useable coordinates x, y if it can.
def can_be_placed(room, top_left_x, top_left_y, side):
    # Do we need to find a place to put the room along the x or y axis?
    test_range = 
    if side == "U" or side == "D":
        range = len(room[0])
    else:
        range = len(room)


    for i in range(len(room)):
        for j in range(len(room[i]):
            if room[i][j] == 1 and dungeon[top_left_x+j][top_left_y+i] != 0:
                return -1

# Generate a room that can be placed
#
# INPUT: x, y coord of ajoining corridor and side "U", "R", "D", "L"
# OUTPUT: room and top_left position if one is found in num_attempts
#         -1 if none can be found.
def find_room(x,y,side):
    tries = 0
    num_attempts = 5
    while tries < num_attempts:
        room = roomGenerator.generate_random_room()
        if can_be_placed(room, x, y, side) != -1:
            return room, can_be_placed(room, x, y, side)
        tries += 1
    return -1, -1, -1

# Generate a room that works and place it in the dungeon
def place_room(x,y,side):
    room, origin_x, origin_y = find_room(x,y,side)


# 100x100 matrix of 0s
dungeon = np.zeros((100,100))

# Add entrance..
dungeon[0,50] = 2
dungeon[1,50] = 2
place_room(2,50,"L")
