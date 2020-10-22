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