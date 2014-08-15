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

def wait_for_button():
    GPIO.wait_for_edge(SPIN, GPIO.FALLING)
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
def step_lock(motor, step_time, direction):
    # Set the direction of the motor
    if direction == "for":
        state = M_FOR
    elif direction == "rev":
        state = M_REV
    else:
        print "Invalid direction in step_lock. Values may be 'for' and 'rev'."
        return False

    # With the options set, run the motor, wait and lock it.
    set_motor_state(motor, state)
    sleep(step_time)
    set_motor_state(motor, (0, 0))
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

if __name__ == "__main__":
    initalize()
    print "Running motor debug mode."
    print "Cycling motor 1."
    step_lock(1, .5, 'for')
    step_lock(1, .5, 'rev')
    print "Cycling motor 2."
    step_lock(2, .5, 'for')
    step_lock(2, .5, 'rev')
    print "Done"
