# Do imports on modules and libraries needed

import numpy as np
import math
from numpy.random import seed
from numpy.random import randint
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Set function to protect secrets
load_dotenv()
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

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
length = 670

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
series = 1

connection = mysql.connector.connect(host='localhost',
                                    database='game_of_life_data',
                                    user='root',
                                    password=MYSQL_PASSWORD)
cursor = connection.cursor()

def close_db():    
    if (connection.is_connected()):
        cursor.close()
        connection.close()

values_for_insertion = []
for i in range(list_length):
    values_for_insertion.append((series, list_length, side, int(grid_values[i]), int(cell_x + i % side), int(cell_y - i//side), 
                           int((cell_x + i % side) + 1), int(cell_y - i//side), 
                           int((cell_x + i % side) + 1), int((cell_y - i//side) - 1),
                           int(cell_x + i % side), int((cell_y - i//side) - 1),
                           int((cell_x + i % side) - 1), int((cell_y - i//side) - 1),
                           int((cell_x + i % side) - 1), int((cell_y - i//side)),
                           int((cell_x + i % side) - 1), int((cell_y - i//side) + 1),
                           int((cell_x + i % side)), int((cell_y - i//side) + 1),
                           int((cell_x + i % side) + 1), int((cell_y - i//side) + 1)))

sql = "INSERT INTO GOL_data (Series, Length, Side, Node_Value, Node_X, Node_Y, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

cursor.executemany(sql, values_for_insertion)
connection.commit()
