# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2  # These are good hints towards reflecting off of the pad...
HALF_PAD_HEIGHT = PAD_HEIGHT / 2  # Use this to constrain the paddles to the drawn board
# in the if statement for paddle collision below.
LEFT = False
RIGHT = True

# Global variables I've added to the template
ball_pos = [WIDTH / 2, HEIGHT / 2]  # Initial position centered in screen
ball_vel = []

paddle1_pos = HEIGHT / 2
paddle1_vel = 0

paddle2_pos = HEIGHT / 2
paddle2_vel = 0
"""
Use this with the key bindings to move the paddle pos... not sure how to link it yet to the 
canvas.line_segments, might have to rely on refresh rate and get that if statement below to 
compare (ball_pos[0] - BALL_RADIUS) to paddle#_pos and then cast reflect... 
"""

score1 = 0
score2 = 0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel  # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]

    if direction == "RIGHT":
        ball_vel = [(random.randrange(2, 4)), - (random.randrange(1, 3))]
    elif direction == "LEFT":
        ball_vel = [- (random.randrange(2, 4)), - (random.randrange(1, 3))]


# define event handlers
def new_game():
    global LEFT, RIGHT  # these are numbers
    global score1, score2  # these are ints
    if LEFT:
        spawn_ball("LEFT")
        LEFT = False
        RIGHT = True
    elif RIGHT:
        spawn_ball("RIGHT")
        LEFT = True
        RIGHT = False


def reset_game():
    global score1, score2
    score1 = 0
    score2 = 0
    new_game()


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel, paddle1_acc, paddle2_acc
    global WIDTH, PAD_WIDTH, HEIGHT, LEFT, RIGHT, HALF_PAD_WIDTH, BALL_RADIUS

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")

    # update paddle's vertical position, keep paddle on the screen
    # Right Paddle Up with restraints
    if (paddle2_pos + HALF_PAD_HEIGHT) >= HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
    else:
        paddle2_pos += paddle2_vel

    # Right Paddle Down with restraints
    if (paddle2_pos - HALF_PAD_HEIGHT) <= 0:
        paddle2_pos = HALF_PAD_HEIGHT
    else:
        paddle2_pos += paddle2_vel

    # Left Paddle Up  with restratints
    if (paddle1_pos + HALF_PAD_HEIGHT) >= HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    else:
        paddle1_pos += paddle1_vel

    # Left Paddle Down with restraints
    if (paddle1_pos - HALF_PAD_HEIGHT) <= 0:
        paddle1_pos = HALF_PAD_HEIGHT
    else:
        paddle1_pos += paddle1_vel

    # draw paddles

    # Left
    canvas.draw_line((HALF_PAD_WIDTH, (paddle1_pos - HALF_PAD_HEIGHT))
                     , (HALF_PAD_WIDTH, (paddle1_pos + HALF_PAD_HEIGHT)), PAD_WIDTH, "White")

    # Right
    canvas.draw_line(((WIDTH - HALF_PAD_WIDTH), (paddle2_pos - HALF_PAD_HEIGHT))
                     , ((WIDTH - HALF_PAD_WIDTH), (paddle2_pos + HALF_PAD_HEIGHT)), PAD_WIDTH, "White")

    # Set Left and Right paddle wall collisions
    if (ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH)):
        # Left Paddle Reflect - Works
        if (ball_pos[1] >= (paddle1_pos - HALF_PAD_HEIGHT)) and (ball_pos[1] <= (paddle1_pos + HALF_PAD_HEIGHT)):
            ball_vel[0] = - (ball_vel[0])
            ball_vel[0] = 1.1 * ball_vel[0]
        else:
            score2 += 1
            RIGHT = True
            LEFT = False
            new_game()

    if (ball_pos[0] >= (WIDTH - (BALL_RADIUS + PAD_WIDTH))):
        # Right Paddle Reflect - Works
        if (ball_pos[1] >= (paddle2_pos - HALF_PAD_HEIGHT) and ball_pos[1] <= (paddle2_pos + HALF_PAD_HEIGHT)):
            ball_vel[0] = -(ball_vel[0])
            ball_vel[0] = 1.1 * ball_vel[0]
        else:
            score1 += 1
            RIGHT = False
            LEFT = True
            new_game()


    # Top wall
    elif ball_pos[1] - BALL_RADIUS <= 0:
        # The top wall casts reflect, it's super effective!
        ball_vel[1] = - (ball_vel[1])
    # Bottom wall
    elif ball_pos[1] + BALL_RADIUS >= HEIGHT:
        # The bottom wall rebukes the ball's freshness.
        ball_vel[1] = - (ball_vel[1])

    # draw scores
    # Draw separate text boxes and send scores correct box
    canvas.draw_text("Player 1: " + str(score1), (20, 20), 20, "White")
    canvas.draw_text("Player 2: " + str(score2), (WIDTH - 100, 20), 20, "White")


def keydown(key):
    global paddle1_vel, paddle1_acc, paddle1_pos
    global paddle2_vel, paddle2_acc, paddle2_pos
    global HALF_PAD_HEIGHT
    paddle1_acc = 2
    paddle2_acc = 2
    if key == simplegui.KEY_MAP["down"]:
        # Key "down" takes paddle2_pos and uses if with height and range and other variables
        # to track paddle position.
        paddle2_vel += paddle2_acc

    if key == simplegui.KEY_MAP["up"]:
        # Key "up" takes (paddle2_pos  - HALF_PAD_HEIGHT) against 0 for restraints, else subtract velocity
        paddle2_vel -= paddle2_acc

    if key == simplegui.KEY_MAP["s"]:
        # Key "s" makes paddle1_pos go down with same restraints as paddle2_pos.
        paddle1_vel += paddle1_acc
        # Key "w" makes paddle1_pos go down also
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= paddle1_acc


def keyup(key):
    global paddle1_vel, paddle2_vel
    # This halts the paddles when the key is let go.
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", reset_game)

# start frame
new_game()
frame.start()