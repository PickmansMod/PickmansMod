import os
import readchar

POS_X = 0
POS_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [3,1]
map_objets = [[2, 3], [5, 4], [3, 4], [10, 6]]

while True:

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            for map_objet in map_objets:
                if map_objet[POS_X] == coordinate_X and map_objet[POS_Y] == coordinate_y
                    
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                print(" @ ", end="")
            else:
                print("   ", end="")
        print("|")
    print("+" + "-" * MAP_WIDTH* 3 + "+")

    #direction = input("¿donde te quieres mover? [WASD]")

    direction = readchar.readchar().decode()

    if direction == "w":
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        my_position[POS_X] -= 1
        my_position(POS_X) %= MAP_WIDTH
    elif direction == "d":
        my_position[POS_X] += 1
        my_position(POS_X) %= MAP_WIDTH
    elif directiion == "q":
        break
    os.system("cls")