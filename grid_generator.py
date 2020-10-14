# Do imports on modules and libraries needed

import numpy as np
import math
from numpy.random import seed
from numpy.random import randint

# Set instance parameters
# Currently the seed is just set to an instance. 
# In future version this might progress through 
# a series. Need to do more research.
#
# seed is the random seed
# length is the number of cells which will be used
# to generate the grid, note that the final number 
# of actual elements in grid may differ from this
# number

seed(1)
length = 100000

# grid_values sets the list as containing 1 or 0
# with an initial list length of the preceding 
# value declaration
# side is called by splitting the list into a
# squared grid with an even number of elements
# per side.

grid_values = randint(0, 2, length)
side = int(length//math.sqrt(length))

print(side)
