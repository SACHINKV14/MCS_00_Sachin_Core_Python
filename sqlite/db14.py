#Drop Table
"""
import sqlite3
#to cteate connection
conn = sqlite3.connect("customers.db")
#create cursor tells what db to do
c=conn.cursor()

c.execute("DROP TABLE customers)
conn.commit()

c.execute("SELECT rowid,* FROM customers ORDER BY rowid DESC liMIT 2")

items=c.fetchall()

for item in items:
    print(item)

#commit our command
conn.commit()
#close our connection
conn.close()
"""