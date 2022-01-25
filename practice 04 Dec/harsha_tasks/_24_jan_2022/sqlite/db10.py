#delete record

import sqlite3
#to cteate connection
conn = sqlite3.connect("customers.db")
#create cursor tells what db to do
c=conn.cursor()


#to delete rowid 2
c.execute("DELETE FROM customers WHERE rowid=2 ")
#commit our command
conn.commit()

c.execute("SELECT rowid,* FROM customers")
#fetch data
items = c.fetchall()  #to fetch all the records
for item in items:   #looping through all records
    print(item)      #get all the items

#close our connection
conn.close()