# Basic motor driver for the pendulum drawing robot.

# Import the rpi gpio module
import RPi.GPIO as GPIO
from time import sleep

# Define motor pins
M1EN = 25
M1A = 23
M1B = 24

M2EN = 22
M2A = 27
M2B = 17

M_OFF = (0, 0)
M_FOR = (1, 0)
M_REV = (0, 1)
M_LOC = (1, 1)

# Start swtich pin
SPIN = 18

# Initalize the GPIO pins
#  Set them to the OUTPUT mode
#  Enable the motors, but turn them off
def initalize():
    GPIO.setmode(GPIO.BCM)
    pins = [M1EN, M1A, M1B, M2EN, M2A, M2B]
    states = [1, 0, 0, 1, 0, 0]
    for ii in range(6):
        pin = pins[ii]
        state = states[ii]
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, state)
    # Initalize our monitor pin - default is down
    GPIO.setup(SPIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    return True

# Kinda silly, but this way we don't have GPIO calls in other fcn's
def wait_for_button(edge):
    if edge == 'falling':
        GPIO.wait_for_edge(SPIN, GPIO.FALLING)
    else:
        GPIO.wait_for_edge(SPIN, GPIO.RISING)
    return True

# Write a given state to a motor
def set_motor_state(motor, state):
    if motor == 1:
        GPIO.output(M1A, state[0])
        GPIO.output(M1B, state[1])
    elif motor == 2:
        GPIO.output(M2A, state[0])
        GPIO.output(M2B, state[1])
    return True
        
# The two useful motor commands
# Motor 1 does the drawing, hence it needs a delta vector
# Motor 2 does the belaying. It steps and then locks

# Step a motor and lock it
def step_lock(motor, step_time, state):
    # With the options set, run the motor, wait and lock it.
    set_motor_state(motor, state)
    sleep(step_time)
    set_motor_state(motor, M_LOC)
    return True

# Given a delta vector, drive the motor
def get_motor_dirn(current_state, pen_down_val, pen_up_val):
    if current_state == pen_down_val:
        state = M_REV
    else:
        state = M_FOR
    return state

def draw_line(motor, vector, pen_down_val, pen_up_val, duration):
    pause_time = duration / len(vector)
    for elem in vector:
        current_state = get_motor_dirn(elem, pen_down_val, pen_up_val)
        set_motor_state(motor, current_state)
        sleep(pause_time)
    return True

def fake_draw_line(dummy_motor, line, pen_down_val, pen_up_val, half_period):
    debug_string = ''
    for elem in line:
        if elem == pen_down_val:
            debug_string += '#'
        else:
            debug_string += ' '
    print debug_string

def draw(image, pen_down_val, pen_up_val, half_period, total_belay_time):
    alternate = False
    print "Release button to start."
    wait_for_button('falling')
    #(row, col) = image.shape()
    # Adjust belay time based on how many lines we have
    belay_time = total_belay_time / 1
    for line in image:
        if alternate:
            line.reverse()
        draw_line(1, line, pen_down_val, pen_up_val, half_period)
        step_lock(2, belay_time, motor.M_FOR)
        # Do some ASCII art so we can see how far we are
        fake_draw_line(1, line, pen_down_val, pen_up_val, half_period)

    # Lift up the pen and return the walker to start
    set_motor_state(1, motor.M_FOR)
    # Rewind the motor until an interrupt on the switch
    set_motor_state(2, motor.M_REV)
    print "Rewinding. Press button to stop."
    wait_for_button('rising')
    set_motor_state(2, motor.M_OFF)
    return True

def demo():
    print "Running motor debug mode."
    print "Cycling motor 1."
    step_lock(1, .5, M_FOR)
    step_lock(1, .5, M_REV)
    print "Cycling motor 2."
    step_lock(2, .5, M_FOR)
    step_lock(2, .5, M_REV)
    print "Done"
    return True

def manual():
    print "Wrapper for motor controls."
    print "TODO: Get fancy about the transforms."
    initalize()
    print "Press button to rewind."
    wait_for_button('rising')
    print "Release button to stop."
    set_motor_state(2, motor.M_REV)
    wait_for_button('rising')
    set_motor_state(2, motor.M_OFF)

if __name__ == "__main__":
    initalize()
    command = 'r'
    while command != 'q':
        # Get user command and break if necesary
        command = raw_input('Command (r, f, q): ')
        if command == 'q':
            break
        # If we want to continue, drive a motor
        motor = int(input('Motor to run (1 or 2): '))
        if command == 'r':
            set_motor_state(motor, M_REV)
        elif command == 'f':
            set_motor_state(motor, M_REV)
        else:
            print "%s is an unsupported command."

        print "Press button to stop."
        wait_for_button('rising')
        set_motor_state(motor, M_OFF)
