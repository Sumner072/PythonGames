# template for "Stopwatch: The Game"
# Import needed libraries and modules
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Define global variables
t = 0
timer_string = '0:00.0'
timer_is_stopped = True
stop_tries = 0
stop_success = 0


# Define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format_time(time):
    a = ((t // 10) // 60)
    b = ((t // 10) % 60) // 10
    c = (t % 100) // 10
    d = (t % 10)
    timer_string = str(a) + ":" + str(b) + str(c) + "." + str(d)

    return timer_string


# define event handlers for buttons; "Start", "Stop", "Reset"
# Start button handler
def start_button_handler():
    if not timer.is_running():
        timer.start()


# Stop button handler
def stop_button_handler():
    global stop_tries
    global stop_success
    if timer.is_running():
        timer.stop()
        stop_tries += 1
        if ((t % 10) == 0):
            stop_success += 1


# Reset button handler
def reset_button_handler():
    global t
    global timer_string
    global stop_tries
    global stop_success
    stop_tries = 0
    stop_success = 0
    timer.stop()
    timer_is_stopped = True
    t = 0
    timer_string = '0:00.0'
    frame.set_draw_handler(canvas_draw_handler)


# define event handler for timer with 0.1 sec interval
def stopwatch_timer_handler():
    global t
    global timer_string
    t += 1
    timer_string = format_time(t)  # Change this to format_time(t) when format_time() is ready.
    frame.set_draw_handler(canvas_draw_handler)


# Define draw handler to canvas
def canvas_draw_handler(canvas):
    global timer_string
    global stop_tries
    global stop_success
    canvas.draw_text(timer_string, (100, 100), 20, "White")
    canvas.draw_text("Successes: " + str(stop_success) + " / Tries: " + str(stop_tries), (30, 130), 20, "White")


# create frame
frame = simplegui.create_frame('Stopwatch Game', 240, 200)

# register event handlers
start_button = frame.add_button('Start', start_button_handler)
stop_button = frame.add_button('Stop', stop_button_handler)
reset_button = frame.add_button('Reset', reset_button_handler)
timer = simplegui.create_timer(100, stopwatch_timer_handler)
frame.set_draw_handler(canvas_draw_handler)

# start frame
frame.start()
