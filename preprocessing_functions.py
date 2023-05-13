# Libraries
import os
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import text
from psycopg2 import sql

os.environ['MPLCONFIGDIR'] = "/home/AQI"
import matplotlib.pyplot as plt

# Settings
import warnings
warnings.filterwarnings("ignore")

def db_connect(dbname):
    # Funktion verbindet die angegebene DB im localhost container
    conn = psycopg2.connect("host=localhost dbname=" + dbname + " user=admin password=secret")

def db_drop_table(dbname, tablename):
    # Funktion verbindet die angegebene DB im localhost container
    conn = psycopg2.connect("host=localhost dbname=" + dbname + " user=admin password=secret")
    cursor = conn.cursor()
    cursor.execute("DROP Table " + tablename)
    conn.commit

# Funktion zur Umwandlung des Datums
def format_date(date_str):
    parts = date_str.split('-')
    return f"{parts[2]}.{parts[1]}.{parts[0][-2:]}"