import generate_random_number
import sqlite3
from datetime import datetime

# Display Date
now = datetime.now()
t = (now.strftime("%Y-%m-%d %H:%M:%S"))

# Define a powerball function

# Create Database
#2
conn = sqlite3.connect("ith.db")
#3
cursor = conn.cursor()

# Create Table
#4
cursor.execute(""" CREATE TABLE loot (date Text, numbers Text)""")



# Print 6 Random lotto numbers


index =0

while index <=2:
    lotto_num = generate_random_number.lotto_numbers(52)
    lotto_num.sort()
    print("Lotto numbers: %s" %(lotto_num))
    l = ''.join(str(lotto_num))


    index +=1
    lot = [(t,l)]
    cursor.executemany("INSERT INTO loot VALUES (?,?)",lot)

    # Save Data 
    conn.commit()
    # Add Data to Database
    #5


# Retrieve Data

for row in cursor.execute('SELECT * FROM loot ORDER BY date'):
    print(row)



