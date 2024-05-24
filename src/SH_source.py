from functions import movable_objects, initialize, game_over, in_game_inputs, game_menu, reinitialize_music
from classes import game, timer
import pygame


# Function that executes the entire game.
def running():

    # While this attribute is true, the next block will be executed.
    while game.reset:

        # Calling the function that initialize the game
        initialize()

        # While this attribute is true, the next block will be executed.
        while game.menu.execute:

            # Execute game_menu function.
            game_menu()

        # Reinitialize music and timer after the player exits the main menu and start playing.
        reinitialize_music()
        timer.reset()

        # While this attribute is true execute the next block.
        while game.execute:

            # Function that reads the user's inputs.
            in_game_inputs()

            # Function that makes every specified object to move.
            movable_objects()

            # Score functions.
            game.show_score()
            game.show_best_score()
            game.new_best_score()

            # Updating the screen.
            pygame.display.flip()

        # Resetting timer to 0.
        timer.reset()

        # While game.over attribute is true, the next block will be executed.
        while game.over:

            game_over()

        # Initialize the game again regardless of the user choice of keep playing or not.
        initialize()

# Calling the function that runs the game
running()
