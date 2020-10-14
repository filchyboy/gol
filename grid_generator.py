# Do imports on modules and libraries needed

import numpy as np
import math
from numpy.random import seed
from numpy.random import randint
from classes import Cell, Node, LinkedList

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
length = 101

# Grid_values sets the list as containing 1 or 0
# with an initial list length of the preceding
# value declaration.
# Side is called by splitting the list into a
# squared grid with an even number of elements
# per side.

grid_values = randint(0, 2, length)
side = int(length//math.sqrt(length))

# Establishing some base values for the building of
# the grid. _x & _y are the coordinates for the cell
# while list_length is the actual number of cells
# in the final grid.

cell_x = 0
cell_y = 0
list_length = side * side

# Call the class instance for a linkedlist

grid_list = LinkedList()

# 

for i in range(list_length):
    grid_list.add_to_head(grid_values[i],
                          cell_x + i % side,
                          cell_y - i//side)
    print(grid_values[i], cell_x + i % side,
                          cell_y - i//side)

grid_list.reverse()
print("Length list:", grid_list.length())
print("Complete list:", grid_list.display())
