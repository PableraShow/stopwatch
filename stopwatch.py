# "Stopwatch: The Game"

import simplegui

# Global variables
time = 0
# counters
score = 0
attempts = 0

# Helper function format that converts time in tenths of seconds
# into formatted string A:BC.D
def format(time):
    # Transform the seconds to minutes
    A = str(time / 600)
    # Get the seconds inside of minutes
    B = str((time % 600) / 100)
    C = str((time % 100) / 10)
    # Get the tenth of minutes
    D = str((time % 10))
    # Return the correct clock format
    return A + ':' + B + C + '.' + D

# Helper function to display successful attempts to stop at x.0
def total(score, attempts):
    return str(score) + '/' + str(attempts)

"""Event handlers for buttons; Start, Stop, Reset"""
# Event handler for start the time
def start_handler():
    # Start timer frame
    timer.start()

# Event handler for stop the time
def stop_handler():
    global score, attempts
    # When click on Stop Button and the time is running
    if timer.is_running():
        # increment the attempt counter
        attempts += 1
        # if time is 0 increment the score counter
        if time % 10 == 0:
            score += 1
    # Stop timer frame
    timer.stop()

# Event handler for reset the time
def reset_handler():
    # Stop timer frame
    timer.stop()
    # re-start the counters
    global time, score, attempts
    time = 0
    score = 0
    attempts = 0
    
# Event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1

# Draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time), (130, 130), 48, '#dddddd')
    canvas.draw_text(total(score, attempts), (290, 48), 30, '#aaaaaa')

# Create frame and timer
frame = simplegui.create_frame('Stopwatch: The Game', 360, 220)
timer = simplegui.create_timer(100, timer_handler)

# Register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button('Start', start_handler, 80)
frame.add_button('Stop', stop_handler, 80)
frame.add_button('Reset', reset_handler, 80)

# Start frame
frame.start()