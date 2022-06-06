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

# for getting current path dynamically
import os


def initiate_map():
    print(" Choose the map: ")
    # perform input of maps logic here

  
    current_directory = os.getcwd()
    
    file = "default.txt"
    path = current_directory+"\maps\\"
    
    MAP = open(f'{path}{file}', "r")
    m = (MAP.read()).split("\n")
    
    
    return

def move(direction):
    
    print()

initiate_map()