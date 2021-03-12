# imports
# global variables
# helper functions
# classes
# event handlers
# create frame
# register event handlers
# start frames and timers

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# Imports
import math
import random
import simplegui

# Global Variables
secret_number = 0
remaining_guesses = 7
# holds status of which range and number of tries are active
active_range_100 = True


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    if active_range_100:
        range100()
    elif not active_range_100:
        range1000()


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global secret_number
    global remaining_guesses
    global active_range_100
    print("Game currently has range 100 and 7 tries.")
    secret_number = random.randrange(0, 100)
    remaining_guesses = 7
    active_range_100 = True


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global secret_number
    global remaining_guesses
    global active_range_100
    print("Game currently has range 1000 and 10 tries.")
    secret_number = random.randrange(0, 1000)
    remaining_guesses = 10
    active_range_100 = False


def input_guess(guess):
    # main game logic goes here
    global secret_number
    global remaining_guesses
    # convert str input to int
    guess_to_int = int(guess)
    # decrement remaining_guesses
    remaining_guesses -= 1
    # main logic for comparing user input and secret_number
    if (remaining_guesses == 0) and (guess_to_int != secret_number):
        print("No more guesses remaining, you lose.  The number was " + str(secret_number) + ". Starting a new game.")
        new_game()
    elif guess_to_int > secret_number:
        print("Guess was " + str(guess_to_int) + ".")
        print("Lower...")
        print("Guesses remaining: " + str(remaining_guesses))
    elif guess_to_int < secret_number:
        print("Guess was " + str(guess_to_int) + ".")
        print("Higher...")
        print("Guesses remaining: " + str(remaining_guesses))
    elif guess_to_int == secret_number:
        print("Guess was " + str(guess_to_int) + ".")
        print("Correct!  Starting a new game...")
        new_game()


# create frame, input, and buttons
muh_frame = simplegui.create_frame('Guess The Number frame', 200, 200)
muh_input = muh_frame.add_input('GTN Input', input_guess, 72)
muh_100_button = muh_frame.add_button('Rangeis[0,100)', range100)
muh_1000_button = muh_frame.add_button('Rangeis[0,1000)', range1000)
# register event handlers for control elements and start frame


# call new_game
new_game()