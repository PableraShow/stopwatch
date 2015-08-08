# "Stopwatch: The Game"

import simplegui

# Global variables
time = 0
# counters
score = 0
attempts = 0

# Helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    # transform the seconds to minutes
    minutes = time // 600
    # get the seconds inside of minutes
    seconds = (time - 600 * minutes) // 10
    # get the tenth of minutes
    tenth = time % 10
    # correct clock format
    if seconds >= 10:
        return str(minutes) + ':' + str(seconds) + '.' + str(tenth)
    else:
        return str(minutes) + ':' + '0' + str(seconds) + '.' + str(tenth)

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
    canvas.draw_text(format(time), (12, 36), 36, 'Red')
    canvas.draw_text(str(score) + '/' + str(attempts) , (150, 36), 24, 'Blue')

# Create frame and timer
frame = simplegui.create_frame('Stopwatch', 200, 140)
timer = simplegui.create_timer(100, timer_handler)

# Register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button('Start', start_handler, 80)
frame.add_button('Stop', stop_handler, 80)
frame.add_button('Reset', reset_handler, 80)

# Start frame
frame.start()


