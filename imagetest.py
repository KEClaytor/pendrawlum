# Load up an example image (stormtrooper.png)
#  and plot it out.

import pygame
import numpy
import pendulo

def load_stormtrooper():
    png = pygame.image.load('stormtrooper.png')
    png = pygame.transform.rotate(stormpng, 90)
    arr = pygame.surfarray.array2d(stormpng)
    whiteval = numpy.amin(arr)
    blackval = numpy.amax(arr) 
    return (arr, whiteval, blackval)

def load_grid():
    png = pygame.image.load('grid.png')
    png = pygame.transform.rotate(stormpng, 90)
    arr = pygame.surfarray.array2d(stormpng)
    whiteval = numpy.amax(arr)
    blackval = numpy.amin(arr) 
    return (arr, whiteval, blackval)

if __name__ == "__main__":

    (imagearr, whiteval, blackval) = load_grid()

    # Half the period of the pendulum
    #  (time for one swing from l->r or r->l, ie; one 'line')
    half_period = 2.00 / 2.0
    # How long to spend belaying the pen to the next line
    belay_time = 0.01
    # And now send it to the write routine
    pendulo.draw(imagearr, whiteval, blackval, half_period, belay_time)

