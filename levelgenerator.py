# Level generator for castle dungeons

import roomGenerator
from corridor import Corridor_generator
import numpy as np
import random

# PARAMETER

MATRIX_DUNGEON_SIZE = 200
MATRIX_CORRIDOR_SIZE = 8
MIN_LENGTH_CORRIDOR = 3
MAX_LENGTH_CORRIDOR = 10
TRY_NUMBER_CORRIDOR = 5
TRY_NUMBER_ROOM = 5





UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

ROOM_FLOOR = 1


def column(matrix, i):
    return [row[i] for row in matrix.getA()]

# Find if a room can be placed and where.
#
# INPUT: same as find_room() but with a candidate room
# OUTPUT: -1 is room cannot be placed
#         useable coordinates x, y if it can. (TOP LEFT)
def can_be_placed(room, x, y, side):
    # Do we need to find a place to put the room along the x or y axis?
    width = len(room.getA()[0])
    height = len(room.getA())
    if side == UP or side == DOWN:
        entry_range = width
    else:
        entry_range = height

    entry_attempt = random.randint(0,entry_range-1)   # Pick a random corridor entry point

    for i in range(entry_range):          # Will try for all possible corridor entries..
        index = 99
        candidate_x = -1
        candidate_y = -1
        # Setup candidate co-ords
        if side == UP or side == DOWN:
            candidate_x = x - (entry_attempt + i) % width

            if side == UP:
                candidate_column = column(room, (entry_attempt + i) % width)
                for index in range(len(candidate_column) -1, -1, -1):
                    if candidate_column[index] == 1:
                        break
                candidate_y = y - index

            else:
                candidate_column = column(room, entry_attempt)
                candidate_y = y - candidate_column.index(1)
        else:
            candidate_y = y - (entry_attempt + i) % height


            if side == LEFT:
                for index in range(len(room.getA()[entry_attempt]) -1, -1, -1):
                    if room.getA()[entry_attempt][index] == 1:
                        break
                candidate_x = x - index


            else:
                for index in range(len(room.getA()[entry_attempt])):
                    if room.getA()[entry_attempt][index] == 1:
                        break
                candidate_x = x - index

        room_placeable = True

        # Check co-ordinates fall within the grid confines..
           # too high or too far left?
        if candidate_x < 0 or candidate_y < 0:
            continue
           # too low or too far right?
        if candidate_x + width >= MATRIX_DUNGEON_SIZE or candidate_y + height >= MATRIX_DUNGEON_SIZE:
          continue

        # Check room is placeable in dungeon for candidate
        for i in range(width):
            for j in range(height):
                if dungeon[candidate_y + j][candidate_x + i] > 0 and room.getA()[j][i] > 0:
                    room_placeable = False
                    break
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
    num_attempts = 1
    while tries < num_attempts:
        room = roomGenerator.generate_random_room()
        for line in room.getA():
            print(line)
        if can_be_placed(room, x, y, side) != -1:
            return room, can_be_placed(room, x, y, side)
        tries += 1
    return -1, -1, -1

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
    entry = None

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

                    if end_direction == UP:
                        entry = DOWN
                    if end_direction == DOWN:
                        entry = UP
                    if end_direction == RIGHT:
                        entry = LEFT
                    if end_direction == LEFT:
                        entry = RIGHT

                    break # finished


    return failure, room, r_top_left_x, r_top_left_y, entry

    return failure

# CHANCE TO GENERATE CORRIDOR:
# FOR EACH GENERATED ROOM:
#   FOR BOTH TOP AND RIGHT WALL:
#       IF NUM_ROOMS == 1:
#           CHANCE OF GENERATING A CORRIDOR = 1
#       ELIF NUM_ROOMS < 7:
#           CHANCE OF GENERATING A CORRIDOR = 0.85
#       ELSE:
#           CHANCE OF GENERATING A CORRIDOR = 0.3 / NUM_ROOMS


cor_generator = Corridor_generator(MATRIX_CORRIDOR_SIZE, MIN_LENGTH_CORRIDOR, MAX_LENGTH_CORRIDOR)

# 100x100 matrix of 0s
dungeon = np.zeros((MATRIX_DUNGEON_SIZE,MATRIX_DUNGEON_SIZE))
room_stack = []

# Add entrance..

dungeon[0,50] = 2
dungeon[1,50] = 2

while room_stack:
    room, r_top_left_x, r_top_left_y, entry = room_stack.pop()
    # for each direction, try to build a corridor

    # for each direction
    for direction in range(4):
        if not entry == direction: #and something probabilistic
            if direction == UP or direction == DOWN:
                rnd = random.randint(0, room.shape[1])
                end_loop = room.shape[0]
            else:
                rnd = random.randint(0, room.shape[0])
                end_loop = room.shape[1]
            # find the coordinate of the right wall
            for i in end_loop:
                if room[i][rnd] == ROOM_FLOOR:
                    break

            if direction == UP:
                x = rnd + r_top_left_x
                y = i+r_top_left_y - 1
            if direction == RIGHT:
                x = rnd + r_top_left_x + 1
                y = i+r_top_left_y
            if direction == DOWN:
                x = rnd + r_top_left_x
                y = i+r_top_left_y + 1
            if direction == LEFT:
                x = rnd + r_top_left_x
                y = i+r_top_left_y - 1

            failure, new_room, new_top_left_x, new_top_left_y, new_entry = generate_corridor_and_room(TRY_NUMBER_CORRIDOR, TRY_NUMBER_ROOM, x, y, UP)
            if not failure:
                room_stack.append((new_room, new_top_left_x, new_top_left_y, new_entry))
            else:
                pass



# for each non entry room, try to place corridor + room
    # Probability of having a a corridor + define the coordinate of the starting corridor
