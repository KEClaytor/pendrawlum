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
    return True

# Write a given state to a motor
def set_motor_state(motor, sa, sb):
    if (sa in [0, 1]) and (sb in [0, 1]):
        if motor == 1:
            GPIO.output(M1A, sa)
            GPIO.output(M1B, sb)
        elif motor == 2:
            GPIO.output(M2A, sa)
            GPIO.output(M2B, sb)
        return True
    else:
        print "Invalid signal to set_motor_state. sa/sb must be either 0 or 1."
        return False
        
# The two useful motor commands
# Motor 1 does the drawing, hence it needs a delta vector
# Motor 2 does the belaying. It steps and then locks

# Step a motor and lock it
def step_lock(motor, step_time, direction):
    # Set the direction of the motor
    if direction == "for":
        sa, sb = (1, 0)
    elif direction == "rev":
        sa, sb = (0, 1)
    else:
        print "Invalid direction in step_lock. Values may be 'for' and 'rev'."
        return False

    # With the options set, run the motor, wait and lock it.
    set_motor_state(motor, sa, sb)
    sleep(step_time)
    set_motor_state(motor, 0, 0)
    return True

# Given a delta vector, drive the motor
def draw_line(vector, pen_down_val, pen_up_val, duration):
    pause_time = duration / length(vector)
    current_state = vector[0]
    if current_state == pen_down_val:
    

if __name__ == "__main__":
    initalize()
    print "Running motor debug mode."
    print "Enabling motor 1."
    print "Cycling motor 1."
    step_lock(1, .5, 'for')
    step_lock(1, .5, 'rev')
    print "Enabling motor 2."
    step_lock(2, .5, 'for')
    step_lock(2, .5, 'rev')
    print "Cycling motor 2."
    print "Disabling all motors."
