import random
import numpy as np

EBR = [["EB", "ER"], ["ETL", "ETL", "ER"], ["ET", "EBR", "ET"], ["EL", "EBL", "EB"], ["ET", "EL", "ETR"]]
EL = [["ETR", "EBL"], ["ETL", "ETR"], ["EL","ETL", "ETL"], ["ETL", "EL", "EL"], ["ER","ETR"]]
EBL = [["EL", "ETL", "EL"], ["ER", "ET", "EB"], ["EB", "ETL"], ["EBR", "EL", "ET"], ["ET", "ETL", "ETL"]]
ETR = [["ET", "ETL", "ER"], ["ER", "EBL", "ER"], ["ER", "EBR", "EL"], ["ER", "EB", "EBL"], ["ET", "ER"]]
ET = [["EB", "EB", "ER"], ["EL", "ER", "EBL"], ["ET", "ER", "ET"], ["EBR","EBR","EL"],["EB", "ETL","ET"]]
ER = [["ER", "EBR", "ETR"], ["EBR", "ET", "ET"], ["EL", "EB", "ETL"],["ET", "EBR"], ["ET","EB"]]
EB = [["ETL", "EBR"], ["ETR", "ER", "EBR"], ["EBL", "ET"], ["EBR", "ET", "EB"], ["ETR", "ER", "ETL"]]
ETL = [["EL","ETR"], ["ETL", "EBL"], ["EBR", "EBR"], ["EB", "EBR"], ["EBR", "ET"]]

def extend_top(room):     # Room is an 8x8 matrix
    if room[3][2] == 0 or room[4][2] == 0:  # If we haven't yet extended bottom
        room[3][2] = 1
        room[4][2] = 1
        return
    if room[3][1] == 0 or room[4][1] == 0:
        room[3][1] = 1
        room[4][1] = 1
        return
    room[3][0] = 1
    room[4][0] = 1

def extend_bottom(room):     # Room is an 8x8 matrix
    if room[3][5] == 0 or room[4][5] == 0:  # If we haven't yet extended bottom
        room[3][5] = 1
        room[4][5] = 1
        return
    if room[3][6] == 0 or room[4][6] == 0:
        room[3][6] = 1
        room[4][6] = 1
        return
    room[3][7] = 1
    room[4][7] = 1

def extend_right(room):
    if room[5][3] == 0 or room[5][4] == 0:
        room[5][3] = 1
        room[5][4] = 1
        return
    if room[6][3] == 0 or room[6][4] == 0:
        room[6][3] = 1
        room[6][4] = 1
        return
    room[7][3] = 1
    room[7][4] = 1

def extend_left(room):
    if room[2][3] == 0 or room[2][4] == 0:
        room[2][3] = 1
        room[2][4] = 1
        return
    if room[1][3] == 0 or room[1][4] == 0:
        room[1][3] = 1
        room[1][4] = 1
        return
    room[0][3] = 1
    room[0][4] = 1

def extend_top_left(room):
    if room[2][3] == 0 or room[2][2] == 0 or room[3][2] == 0:
        room[2][3] = 1
        room[2][2] = 1
        room[3][2] = 1
        return
    if room[1][2] == 0 or room[1][1] == 0 or room[2][1] == 0:
        room[1][2] = 1
        room[1][1] = 1
        room[2][1] = 1
        return
    room[0][1] = 1
    room[0][0] = 1
    room[1][0] = 1

def extend_top_right(room):
    if room[5][3] == 0 or room[5][2] == 0 or room[4][2] == 0:
        room[5][3] = 1
        room[5][2] = 1
        room[4][2] = 1
        return
    if room[6][2] == 0 or room[6][1] == 0 or room[5][1] == 0:
        room[6][2] = 1
        room[6][1] = 1
        room[5][1] = 1
        return
    room[7][1] = 1
    room[7][0] = 1
    room[6][0] = 1

def extend_bottom_left(room):
    if room[2][4] == 0 or room[2][5] == 0 or room[3][5] == 0:
        room[2][4] = 1
        room[2][5] = 1
        room[3][5] = 1
        return
    if room[1][5] == 0 or room[1][6] == 0 or room[2][6] == 0:
        room[1][5] = 1
        room[1][6] = 1
        room[2][6] = 1
        return
    room[0][6] = 1
    room[0][7] = 1
    room[1][7] = 1

def extend_bottom_right(room):
    if room[4][5] == 0 or room[5][5] == 0 or room[5][4] == 0:
        room[4][5] = 1
        room[5][5] = 1
        room[5][4] = 1
        return
    if room[5][6] == 0 or room[6][6] == 0 or room[6][5] == 0:
        room[5][6] = 1
        room[6][6] = 1
        room[6][5] = 1
        return
    room[6][7] = 1
    room[7][7] = 1
    room[7][6] = 1

def generate():
    room = [[],[],[],[],[],[],[],[]]
    for i in range(len(room)):
        line = []
        for j in range(8):
            line += [0]
        room[i] = line
    room[3][3] = 1
    room[3][4] = 1
    room[4][3] = 1
    room[4][4] = 1

    num_instruction_sets = random.randint(2,5)
    for i in range(num_instruction_sets):
        ops = random.choice(random.choice([EB,ET,ER,EL,ETR,ETL,EBR,EBL]))
        for blah in ops:
            if blah == "EB":
                extend_bottom(room)
            elif blah == "ER":
                extend_right(room)
            elif blah == "EL":
                extend_left(room)
            elif blah == "ET":
                extend_top(room)
            elif blah == "ETR":
                extend_top_right(room)
            elif blah == "ETL":
                extend_top_left(room)
            elif blah == "EBL":
                extend_bottom_left(room)
            else:
                extend_bottom_right(room)

    # Find bounding box
    max_i = 4
    min_i = 3
    max_j = 4
    min_j = 3
    for i in range(4,-1,-1):
        if 1 in room[i]:
            min_i = i
    for i in range(4,8):
        if 1 in room[i]:
            max_i = i

    for j in range(4,-1,-1):
        for i in range(8):
            if room[i][j] == 1:
                min_j = j
    for j in range(4,8):
        for i in range(8):
            if room[i][j] == 1 and j > max_j:
                max_j = j

    # Strip bounding box
    bounded = []
    for i in range(min_j, max_j+1):
        line = []
        for j in range(min_i, max_i+1):
            if room[j][i] == 0 or room[j][i] == 1:
                line += [room[j][i]]
        bounded += [line]

    return_matrix = np.matrix(bounded)
    return return_matrix
