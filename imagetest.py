# Load up an example image (stormtrooper.png)
#  and plot it out.

import pygame
import numpy
import pendulo

if __name__ == "__main__":
    stormpng = pygame.image.load('stormtrooper.png')
    stormarr = pygame.surfarray.array2d(stormpng)
    whiteval = numpy.amax(stormarr)
    blackval = numpy.amin(stormarr) 

    # Half the period of the pendulum
    #  (time for one swing from l->r or r->l, ie; one 'line')
    half_period = 2.00
    # How long to spend belaying the pen to the next line
    belay_time = 0.1
    # And now send it to the write routine
    pendulo.draw(stormarr, whiteval, blackval, half_period, belay_time)

