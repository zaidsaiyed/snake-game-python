'''
TODO
Game loop
    Game intitalization
    Game end
Move snake

Eating snake

MAP
Food
Rules
Score

UI

'''

# This file has all game attributes


import os
import random
from time import sleep
from pytimedinput import timedInput


def initiate_map():
    # perform input of maps logic here
    print("Choose the map: ")
    print("\n 1 = Default")
    #map_selection = input("Choose map number: ")
    current_directory = os.getcwd()
    file = "default.txt"
    path = current_directory+"\maps\\"
    
    MAP = open(f'{path}{file}', "r+")
    MAP.seek(0)
    return MAP


def scan_map(map):
    list_of_lines = map.read().split("\n")
    working_area = list_of_lines[1:-1]
    
def detect_direction():
    
    input, _ = timedInput("",0.3)
    
    if input.lower() == "s":
        direction = 'down'
        move_snake(map, direction)
        
def food(map):
    food_position = random.choice(valid_pos)
    map.seek(food_position)
    map.write("$")
    os.system('cls')
    print_map(map)
    
    return food_position



def direction_to_move(map, direction, new_pos, food_pos):
    score = 0
    temp = 34
    snake_pos = []
    while True:
        if new_pos in valid_pos:
            old_pos = temp
            map.seek(new_pos)
            map.write('O')
            
            os.system('cls')
            print_map(map)
            #sleep(0.25)
            
            map.seek(old_pos)
            map.write(' ')
            
            match direction:
                case 'd':
                    
                    new_pos += 1
                    snake_pos.insert(0,new_pos)
                    direction, _ = timedInput("",0.15)
                    if direction == '':
                        direction = 'd'
                    
                    # To increase food    
                    if new_pos == food_pos:
                        new_food_pos = food(map)
                        food_pos = new_food_pos
                        score += 1
                    else:
                        temp = snake_pos.pop()
                        
                case 'a':
                    
                    new_pos -= 1
                    snake_pos.insert(0,new_pos)
                    direction, _ = timedInput("",0.15)
                    if direction == '':
                        direction = 'a'
                        
                    if new_pos == food_pos:
                        new_food_pos = food(map)
                        food_pos = new_food_pos
                        score += 1
                    else:
                        temp = snake_pos.pop()
                        
                case 'w':
                    
                    new_pos -= 33
                    snake_pos.insert(0,new_pos)
                    direction, _ = timedInput("",0.25)
                    if direction == '':
                        direction = 'w'
                        
                    if new_pos == food_pos:
                        new_food_pos = food(map)
                        food_pos = new_food_pos
                        score += 1
                    else:
                        temp = snake_pos.pop()
                        
                case 's':
                    
                    new_pos += 33
                    snake_pos.insert(0,new_pos)
                    direction, _ = timedInput("",0.25)
                    if direction == '':
                        direction = 's'
                        
                    if new_pos == food_pos:
                        new_food_pos = food(map)
                        food_pos = new_food_pos
                        score += 1
                    else:
                        temp = snake_pos.pop()
            
        else:
            break
    return score

valid_pos = [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359]
invalid_pos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 63, 64, 65, 66, 96, 97, 98, 99, 129, 130, 131, 132, 162, 163, 164, 165, 195, 196, 197, 198, 228, 229, 230, 231, 261, 262, 263, 264, 294, 295, 296, 297, 327, 328, 329, 330, 360]

def move_snake(map):
    food_pos = food(map)
    
    START_POS = 34
    new_pos = START_POS
    
    os.system('cls')
    print_map(map)
    
    initial = True
    game_running = True
    
    direction = 'd'
    while game_running:
        
        score = direction_to_move(map, direction, new_pos, food_pos)
        
        print_score(score)
        game_running = False
        break

            
    
def print_map(map):
    map.seek(0)
    list_of_lines = map.read().split("\n")
    for line in list_of_lines:
        print(line)

def game_over():
    os.system('cls')
    current_directory = os.getcwd()
    file = "game_over.txt"
    path = current_directory+"\\"
    
    game_over_txt = open(f'{path}{file}', "r")
    
    list_of_lines = game_over_txt.read().split("\n")
    for line in list_of_lines:
        print(line)
        
def print_score(score):
    for _ in range(3):
        os.system('cls')
        sleep(0.5)
        game_over()
        sleep(0.7)
        
    os.system('cls')
    sleep(0.7)
    print('\n\n\nYour score is:', score)
    print()
    print()
    print()
    