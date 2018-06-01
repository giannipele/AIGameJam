# Level generator for castle dungeons

import roomGenerator
from corridor import Corridor_generator
import numpy as np
import random



UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Find if a room can be placed and where.
#
# INPUT: same as find_room() but with a candidate room
# OUTPUT: -1 is room cannot be placed
#         useable coordinates x, y if it can.
def can_be_placed(room, top_left_x, top_left_y, side):
    # Do we need to find a place to put the room along the x or y axis?
    test_range = 8
    if side == "U" or side == "D":
        range = len(room[0])
    else:
        range = len(room)


    for i in range(len(room)):
        for j in range(len(room[i]):
            if room[i][j] == 1 and dungeon[top_left_x+j][top_left_y+i] != 0:
                return False


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



# x_d, y_d : coordinate of the starting point's corridor in the dungeon matrix(the first corridor's tile), 
# x_c, y_c: coordinate of the starting point's corridor in the corridor matrix 
def corridor_can_be_placed(corridor_matrix, x_d, y_d, x_c, y_c):
    failure = False
    finish = False
    
    while not finish:
        # check around the current point's corridor to get the next point
        direction = None

        if y_c + 1 < corridor_matrix.shape[0] and corridor_matrix[y_c+1][x_c] == 1:
            direction = DOWN
            y_c += 1
        elif y_c - 1 >= 0 and corridor_matrix[y_c-1][x_c] == 1:
            direction = UP
            y_c -= 1
        elif x_c + 1 < corridor_matrix.shape[1] and corridor_matrix[y_c][x_c+1] == 1:
            direction = RIGHT
            x_c += 1
        elif x_c - 1 >= 0 and corridor_matrix[y_c][x_c-1] == 1:
            direction = LEFT
            x_c -= 1
        else:
            finish = True


        # check if the next point is a 0 in the dungeon matrix
        if not finish:
            if y_d+1 <= dungeon.shape[0] direction == DOWN and dungeon[y_d+1][x_d] == 0:
                y_d += 1
            elif y_d-1 >= 0 and direction == UP and dungeon[y_d-1][x_d] == 0:
                y_d -= 1
            elif x_d+1 <= dungeon.shape[1] and direction == RIGHT and dungeon[y_d][x_d+1] == 0:
                x_d += 1
            elif x_d - 1 >= 0 and direction == LEFT and dungeon[y_d][x_d-1] == 0:
                x_d -= 1
            else:
              failure = True

        if failure:
            finish = True

    return not failure


def generate_corridor_and_room(n, m, x, y, direction):
    failure = False

    for _ in range(n):
        corridor, ending_point, end_direction = cor_generator.generate(direction)
        if corridor_can_be_placed(corridor, x, y, ending_point[0], ending_point[1]):
            # generate and place the room





cor_generator = Corridor_generator(10, 3, 13)

# 100x100 matrix of 0s
dungeon = np.zeros((100,100))
room_stack = []

# Add entrance..
dungeon[0,50] = 2
dungeon[1,50] = 2
place_room(2,50,"L")


# for each non entry room, try to place corridor + room
    # Probability of having a a corridor + define the coordinate of the starting corridor







