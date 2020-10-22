# Table Creator
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