# Import the motor module and prepare to draw
import pygame
import numpy
import motor

# Return a black/white array for a file
#  with the black/white values
def load_image(image_string):
    png = pygame.image.load(image_string)
    png = pygame.transform.rotate(png, 90)
    arr = pygame.surfarray.array2d(png)
    whiteval = numpy.amin(arr)
    blackval = numpy.amax(arr) 
    return (arr, whiteval, blackval)

if __name__ == "__main__":

    (imagearr, whiteval, blackval) = load_image('grid.png')

    # Half the period of the pendulum
    #  (time for one swing from l->r or r->l, ie; one 'line')
    half_period = 2.00 / 2.0
    # How long to spend belaying the pen to the next line
    belay_time = 0.1
    # And now send it to the write routine
    motor.draw(imagearr, whiteval, blackval, half_period, belay_time)

