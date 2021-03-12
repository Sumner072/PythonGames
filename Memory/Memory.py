# implementation of card game - Memory
# Currently completed: Step 8

import random

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Global variables
list_a = list(range(0, 8))
# print list_a
list_b = list(range(0, 8))
# print list_b
card_nums = list_a + list_b

# Shuffle the list contents
random.shuffle(card_nums)
# print card_nums

# Variable 'exposed' for T/F list to determine card drawing.
exposed = [False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False, False, False]
# print exposed

# Card index number, get from dividing pos[0] by 50 into int in the mouseclick handler.
card_index = 0
total_turns = 0


# helper function to initialize globals
def new_game():
    global card_state, total_turns, exposed
    total_turns = 0
    card_state = 0
    exposed = [False, False, False, False, False, False, False, False, False,
               False, False, False, False, False, False, False, False, False]


# define event handlers
def mouseclick(pos):
    global exposed, card_state, last_card, new_card, total_turns
    card_index = pos[0] // 50
    if exposed[card_index]:
        # Using return exits the function, whereas pass goes to the next thing in the function, causing a glitch.
        return

    # add game state logic here
    if card_state == 0:
        last_card = None
        card_state = 1
    elif card_state == 1:
        last_card = new_card
        total_turns += 1
        card_state = 2
    else:
        if card_nums[last_card] != card_nums[new_card]:
            exposed[last_card] = False
            exposed[new_card] = False
        last_card = None
        card_state = 1

    # Set boolean value to expose selected card.
    if not exposed[card_index]:
        exposed[card_index] = True
    else:
        exposed[card_index] = False
    # print exposed
    new_card = card_index
    exposed[card_index] = True


# cards are logically 50x100 pixels in size
def draw(canvas):
    global card_nums, exposed
    # print card_nums

    for i in range(len(card_nums)):
        # Draw all the numbers
        canvas.draw_text(str(card_nums[i]), (((i * 50) + 25), 50), 20, "White")
        # Draw green boxes over numbers
        if not exposed[i]:
            canvas.draw_polygon([[((i * 50)), 0], [((i * 50)), 100], [(((i + 1) * 50)), 100],
                                 [(((i + 1) * 50)), 0]], 1, "White", "Green")

    label.set_text("Turns = " + str(total_turns))


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()