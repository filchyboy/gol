import numpy as np
import math
from numpy.random import seed
from numpy.random import randint
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import pandas as pd

# Set function to protect secrets
load_dotenv()
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

# Create dataframe
column_names = ["Series", "Length", "Side", "Node_Value",
                "Node_X", "Node_Y", "x1", "y1", "x2", "y2",
                "x3", "y3", "x4", "y4", "x5", "y5", "x6",
                "y6", "x7", "y7", "x8", "y8"]

df = pd.DataFrame(columns = column_names)

connection = mysql.connector.connect(host='localhost',
                                    database='game_of_life_data',
                                    user='root',
                                    password=MYSQL_PASSWORD)
cursor = connection.cursor()

query = ("SELECT Series, Length, Side, Node_Value, Node_X, Node_Y, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8 FROM GOL_data")
cursor.execute(query)
for (Series, Length, Side, Node_Value, Node_X, Node_Y, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8) in cursor:
    df = df.append({'Series': Series, 'Length': Length, 'Side': Side,
                    'Node_Value': Node_Value, 'Node_X': Node_X,
                    'Node_Y': Node_Y, 'x1': x1, 'y1': y1, 'y2': y2,
                    'x2': x2, 'x3': x3, 'y3': y3, 'x4': x4,
                    'y4': y4, 'x5': x5, 'y5': y5, 'x6': x6,
                    'y6': y6, 'x7': x7, 'y7': y7, 'x8': x8,
                    'y8': y8}, ignore_index=True)



grid = []
node_list = {}
node_df = []
field_of_grid = []
for i in range(len(df)):
  grid.append([i, df['Series'][i], df['Length'][i], df['Side'][i],
               df['Node_Value'][i], df['Node_X'][i], df['Node_Y'][i],
               [df['x1'][i], df['y1'][i]], 
               [df['x2'][i], df['y2'][i]], 
               [df['x3'][i], df['y3'][i]], 
               [df['x4'][i], df['y4'][i]],
               [df['x5'][i], df['y5'][i]],
               [df['x6'][i], df['y6'][i]],
               [df['x7'][i], df['y7'][i]],
               [df['x8'][i], df['y8'][i]]
               ])
  node_list[str([df['Node_X'][i], df['Node_Y'][i]])] = df['Node_Value'][i]
  node_df.append([ [df['Node_X'][i], df['Node_Y'][i]], df['Node_Value'][i]])
field_of_grid = df

df = df.drop(['Series', 'Length', 'Side', 'Node_Value', 'Node_X', 'Node_Y'], 1)

field_of_grid = np.array(df)
field_of_node = np.array(node_df)
grid_df = pd.DataFrame(data=grid, columns=['i', 'series', 'length', 'side', 'value', 'x', 'y', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8'])


def search_eight(x, y):
  '''
Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

  '''
  global count, reproduction_list, original_seed
  for each in range(len(node_df)):
    node_growth = str(node_df[each][1])
    for i in range(9 - 1):
      count = count + node_list.get(str(grid[each][i + 7]), 0)
      original_seed.append([node_list.get(str(grid[each][i + 7]), 0)])
    if count <= 1: node_growth = 0
    if count == 2 or 3: node_growth = 1
    if count >= 4: node_growth = 0
    count = 0

    reproduction_list.append(node_growth)
original_seed = []
reproduction_list = []
count = 0
num = len(grid)
def parse_grid(arr):
  global num
  while num == 0:
    return
  else:
    search_eight(grid[num - 1][5], grid[num - 1][6])
    num -= 100
    # parse_grid(grid)

parse_grid(grid)

print(type(original_seed[0][0]))

# values_for_insertion = []
# for i in range(len(original_seed)):
#     values_for_insertion.append((series, list_length, side, original_seed[][0]))

# sql = "INSERT INTO GOL_data (Series, Length, Side, Node_Value, Node_X, Node_Y, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

# cursor.executemany(sql, values_for_insertion)
# connection.commit()