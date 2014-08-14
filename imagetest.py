# Load up an example image (stormtrooper.png)
#  and plot it out.

import pygame
import pendulo

if __name__ == "__main__":
    stormpng = pygame.image.load('stormtrooper.png')
    stormarr = pygame.surfarray.array2d(stormpng)
    whiteval = numpy.amax(stormarr)
    blackval = numpy.amin(stormarr) 

    # And now send it to the write routine
    pendulo.draw(stormarr, maxval, minval)
