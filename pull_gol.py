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

connection = mysql.connector.connect(host='localhost',
                                    database='game_of_life_data',
                                    user='root',
                                    password=MYSQL_PASSWORD)
cursor = connection.cursor()

query = ("SELECT Series, Length, Side, Node_Value, Node_X, Node_Y, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8 FROM GOL_data")
cursor.execute(query)
for (Series, Length, Side, Node_Value, Node_X, Node_Y, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8) in cursor:
    print(Series, Length, Side, Node_Value, Node_X, Node_Y, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8)
