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

    return 0, 0


# Generate a room that works and place it in the dungeon
def place_element(element, r_top_left_x, r_top_left_y):

    for i in range(element.shape[0]):
        for j in range(element.shape[1]):
            if element[i][j] != 0:
                # copy it in the dungeon matrix
                dungeon[i+r_top_left_y][j+r_top_left_x] = element[i][j]



# x_d, y_d : coordinate of the starting point's corridor in the dungeon matrix(the first corridor's tile), 
# x_c, y_c: coordinate of the starting point's corridor in the corridor matrix 
def corridor_can_be_placed(corridor_matrix, x_d, y_d, x_c, y_c):
    failure = False
    finish = False
    
    last_direction = None

    while not finish:
        # check around the current point's corridor to get the next point
        direction = None

        if last_direction != UP and y_c + 1 < corridor_matrix.shape[0] and corridor_matrix[y_c+1][x_c] != 0:
            direction = DOWN
            y_c += 1
        elif last_direction != DOWN and y_c - 1 >= 0 and corridor_matrix[y_c-1][x_c] != 0:
            direction = UP
            y_c -= 1
        elif last_direction != LEFT and x_c + 1 < corridor_matrix.shape[1] and corridor_matrix[y_c][x_c+1] != 0:
            direction = RIGHT
            x_c += 1
        elif last_direction != RIGHT and x_c - 1 >= 0 and corridor_matrix[y_c][x_c-1] != 0:
            direction = LEFT
            x_c -= 1
        else:
            finish = True


        # check if the next point is a 0 in the dungeon matrix
        if not finish:
            if y_d+1 <= dungeon.shape[0] and direction == DOWN and dungeon[y_d+1][x_d] == 0:
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

        last_direction = direction

    return not failure


def generate_corridor_and_room(n, m, x, y, direction):
    failure = True

    for _ in range(n):
        corridor, ending_point, starting_point, end_direction = cor_generator.generate(direction)
        if corridor_can_be_placed(corridor, x, y, starting_point[0], starting_point[1]):
            for __ in range(m):
                room = roomGenerator.generate_random_room()
                r_top_left_x, r_top_left_y = room_can_be_placed(room, ending_point[0], ending_point[1], direction)
                if d_top_left_x != -1:

                    # get the topleft coordinate of the corridor matrix IN the dungeon matrix
                    c_top_left_x = x - starting_point[0]
                    c_top_left_y = y - starting_point[1]
                    # place the room
                    place_relement(room, r_top_left_x, r_top_left_y)
                    place_element(corridor, c_top_left_x, c_top_left_y)
                    failure = False
                    break # finished

    
    return failure   




# cor_generator = Corridor_generator(10, 3, 13)

# # 100x100 matrix of 0s
dungeon = np.zeros((50,50))
room_stack = []

# # Add entrance..
# dungeon[0,50] = 2
# dungeon[1,50] = 2
# place_room(2,50,"L")


# for each non entry room, try to place corridor + room
    # Probability of having a a corridor + define the coordinate of the starting corridor







