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
    
    MAP = open(f'{path}{file}', "r")
    return MAP


def scan_map(map):
    list_of_lines = map.read().split("\n")
    working_area = list_of_lines[1:-1]
    # print(len(working_area[1]))
    # snake = '▒'
    # print(snake)
        
    
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

