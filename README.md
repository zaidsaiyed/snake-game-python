# Snake Game

This is a simple console-based implementation of the classic Snake game using Python. The game is played on a 20x20 grid, with the player controlling a snake that grows longer as it eats food. The game ends if the snake collides with a wall or with its own body.

## Installation

To run this game, you'll need to have Python 3 installed on your computer. You can download the latest version of Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

You'll also need to install the `pytimedinput` module, which can be installed using pip:
```
pip install pytimedinput
```
Once you have Python and `pytimedinput` installed, you can run the game by executing the `snake.py` file:
```
python snake.py
```

## How to Play

When you start the game, you'll see a 20x20 grid with a snake and some food. You can control the snake using the arrow keys:

-   Up arrow: move the snake up
-   Down arrow: move the snake down
-   Left arrow: move the snake left
-   Right arrow: move the snake right

The snake will move automatically in the direction it is facing. If the snake's head collides with a wall or with its own body, the game ends. If the snake's head collides with food, it will eat the food and grow longer.

The goal of the game is to eat as much food as possible without colliding with a wall or with the snake's own body.

## Code Explanation

The `snake.py` file contains all of the game logic. Here's a brief explanation of the code:

-   `initiate_map()`: This function initializes the game map by reading a text file that contains the map layout.
-   `detect_direction()`: This function listens for input from the user and moves the snake in the corresponding direction.
-   `food()`: This function generates food at a random location on the map.
-   `valid_pos` and `invalid_pos`: These lists contain the valid and invalid positions on the map, respectively.
-   The `while` loop in the `main()` function is the game loop, which runs until the game ends.
-   The `scan_map()` function reads the map text file and extracts the working area of the game map.
-   The `move_snake()` function moves the snake by erasing its previous position and drawing it in its new position.
-   The `eating_snake()` function checks if the snake has collided with food and updates the score and snake length accordingly.
-   The `print_map()` function prints the game map to the console.

## Credits

This game was created by Zaid Saiyed and is based on the classic retro Snake game. The game logic and console interface were implemented using Python.
