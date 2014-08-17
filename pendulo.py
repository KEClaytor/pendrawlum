# Import the motor module and prepare to draw
import pygame
import numpy
import motor
import math

# Return a black/white array for a file
#  with the black/white values
def load_image(image_string):
    png = pygame.image.load(image_string)
    png = pygame.transform.rotate(png, 90)
    arr = pygame.surfarray.array2d(png)
    whiteval = numpy.amin(arr)
    blackval = numpy.amax(arr) 
    return (arr, whiteval, blackval)

# Wait until the mouse returns a relative difference with sign
def get_mouse_sign():
    (x,y) = pygame.mouse.get_rel()
    math.copysign(sign_x, x)
    return sign_x

def wait_for_mouse(sign):
    # Allow arbitrary mouse bounds
    pygame.mouse.set_visible(False)
    while get_mouse_sign() != sign:
        pause(0.01)
    return True
    
def draw(image, pen_down_val, pen_up_val, half_period, total_belay_time):
    alternate = False
    #(row, col) = image.shape()
    # Adjust belay time based on how many lines we have
    belay_time = total_belay_time / 1
    for line in image:
        wait_for_mouse(1)
        #if alternate:
        #    line.reverse()
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

if __name__ == "__main__":

    while True:
        print "Release button to start."
        wait_for_button('falling')
        (imagearr, whiteval, blackval) = load_image('grid.png')

        # Half the period of the pendulum
        #  (time for one swing from l->r or r->l, ie; one 'line')
        half_period = 2.00 / 2.0
        # How long to spend belaying the pen to the next line
        belay_time = 0.1
        # And now send it to the write routine
        motor.draw(imagearr, whiteval, blackval, half_period, belay_time)

