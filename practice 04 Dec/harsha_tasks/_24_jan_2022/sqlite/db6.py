#formatiing results
#Query and fetch all
import sqlite3
#to cteate connection
conn = sqlite3.connect("customers.db")
#create cursor tells what db to do
c=conn.cursor()

#query the database
c.execute("SELECT * FROM customers")

#fetch data
items = c.fetchall()  #to fetch all the records
for item in items:   #looping through all records
    print(item)      #get all the items
    print(item[0])   #get only first
    print(item[0]+"\t"+item[1]+"\t\t"+item[2])



#commit our command
conn.commit()
#close our connection
conn.close()