import sqlite3
import csv

def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of lists
    containing rows in the csv file and its entries.
    """
    with open(csvfilename, encoding='utf-8') as csvfile:
        rows = [row for row in csv.reader(csvfile)]
    return rows


conn = sqlite3.connect('food_options.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table to store the food options

# cursor.execute('''CREATE TABLE food_options
#                (id INTEGER PRIMARY KEY,
#                name TEXT,
#                price REAL)''')

#already created

data = read_csv("menu.csv")[1:]

print(data)
cursor.executemany("INSERT INTO food_options (id, name, price) VALUES (?, ?, ?)", data)



conn.commit()


