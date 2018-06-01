# Level generator for castle dungeons

import roomGenerator
from corridor import Corridor_generator
import numpy as np
import random

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def column(maxtrix, i):
    return [row[i] for row in matrix]

# Find if a room can be placed and where.
#
# INPUT: same as find_room() but with a candidate room
# OUTPUT: -1 is room cannot be placed
#         useable coordinates x, y if it can. (TOP LEFT)
def can_be_placed(room, x, y, side):
    # Do we need to find a place to put the room along the x or y axis?
    width = len(room[0])
    height = len(room)
    if side == UP or side == DOWN:
        entry_range = width
    else:
        entry_range = height

    entry_attempt = random.randint(0,entry_range)   # Pick a random corridor entry point

    for i in range(entry_range):          # Will try for all possible corridor entries..
        candidate_x = -1
        candidate_y = -1
        # Setup candidate co-ords
        if side == UP or side == DOWN:
            candidate_x = x - (entry_attempt + i) % width
            if side == UP:
                #FIXME
                candidate_column = column(room, entry_attempt)
                for index in range(len(candidate_column), -2, -1):
                    if candidate_column[index] == 1:
                        break
                # FIND LAST INDEX OF 0
                if index == -1:
                    continue
                candidate_y = y + height - index

            else:
                #FIXME
                candidate_y = y
        else:
            candidate_y = y - (entry_attempt + i) % height
            if side == LEFT:
                for index in range(len(room[entry_attempt]), -2, -1):
                    if room[entry_attempt][index] == 1:
                        break
                # FIND LAST INDEX OF 0
                if index == -1:
                    continue
                candidate_x = x - width + index
            else:
                candidate_y = x - room[entry_attempt].index(i)
        room_placeable = True
        print("CANDIDATES:",candidate_x, candidate_y)

        # Check co-ordinates fall within the grid confines..
           # too high or too far left?
        if candidate_x < 0 or candidate_y < 0:
            continue
           # too low or too far right?
        if candidate_x + width >= 1000 or candidate_y + height >= 1000:
          continue

        # Check room is placeable in dungeon for candidate
        for i in range(width):
            for j in range(height):
                if dungeon[candidate_y + j][candidate_x + i] > 0 and room[j][i] > 0:
                    room_placeable = False
        # Return if successful.
        if room_placeable:
            return candidate_x, candidate_y

    # Else return -1,-1
    return -1, -1


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
"""def corridor_can_be_placed(corridor_matrix, x_d, y_d, x_c, y_c):
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
"""
# 100x100 matrix of 0s
dungeon = np.zeros((100,100))
room_stack = []

# Add entrance..
dungeon[0,50] = 2
dungeon[1,50] = 2
print(find_room(2,50,DOWN))
#place_room(2,50,"L")


# for each non entry room, try to place corridor + room
    # Probability of having a a corridor + define the coordinate of the starting corridor
