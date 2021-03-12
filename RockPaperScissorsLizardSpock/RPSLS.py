# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# modules needed
import random


# helper functions

def name_to_number(name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print("An incorrect name was used in the name_to_number function.")


def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print("An incorrect number was used in the number_to_name function.")


def rpsls(player_choice):
    # print a blank line to separate consecutive games
    print()

    # print out the message for the player's choice
    print("Player chooses " + player_choice)

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)

    # print out the message for computer's choice
    print("Computer chooses " + comp_choice)

    # compute difference of comp_number and player_number modulo five
    moddifference = (player_number - comp_number) % 5

    # use if/elif/else to determine winner, print winner message
    if (moddifference == 1) or (moddifference == 2):
        print("Player wins!")
    elif (moddifference == 3) or (moddifference == 4):
        print("Computer Wins!")
    else:
        print("Player and computer tie!")


# testing code
rpsls("rock")
rpsls("paper")
rpsls("scissors")
rpsls("lizard")
rpsls("Spock")
