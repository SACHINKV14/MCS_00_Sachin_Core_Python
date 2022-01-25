#Limiting Results

import sqlite3
#to cteate connection
conn = sqlite3.connect("customers.db")
#create cursor tells what db to do
c=conn.cursor()


#print two records
# c.execute("SELECT rowid,* FROM customers liMIT 2")
#ordeing by rowid and also limiting to 2 records
c.execute("SELECT rowid,* FROM customers ORDER BY rowid DESC liMIT 2")

items=c.fetchall()

for item in items:
    print(item)

#commit our command
conn.commit()
#close our connection
conn.close()