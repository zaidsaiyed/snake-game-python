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
from time import sleep


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
    map.seek(62)
    map.write('O')
    # print(len(working_area[1]))
    # snake = '▒'
    # print(snake)
    
def move_snake(map, direction):
    
    v = range(34,63)
    valid_pos=[]
    
    START_POS = 34
    new_pos = START_POS
    if direction == 'right':
        # key press logic
        while new_pos != 0:
            map.seek(new_pos)
            map.write('O')
            new_pos += 1
            if new_pos == 0:
                pass
    
        
    
def print_map(map):
    map.seek(0)
    list_of_lines = map.read().split("\n")
    for line in list_of_lines:
        print(line)
    # sleep(0.5)
    # os.system('cls')
    # print("hi")

def move(direction):
    
    if direction == 0:
        pass

