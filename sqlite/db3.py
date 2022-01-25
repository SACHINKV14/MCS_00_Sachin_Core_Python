#insert one recoord into the table

import sqlite3

#to cteate connection
conn = sqlite3.connect("customers.db")

#create cursor tells what db to do
c=conn.cursor()
#Insert data into table
c.execute("INSERT INTO customers VALUES ('shewag','s','sewag.s@gmail.com')")


print("command executed succesfully...")
#commit our command
conn.commit()

#close our connection
conn.close()