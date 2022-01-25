#primary key id(unique id where each record gets)
#primary key is created by sqlite
#Query and fetch all
import sqlite3
#to cteate connection
conn = sqlite3.connect("customers.db")
#create cursor tells what db to do
c=conn.cursor()

#query the database add rowid here to get rowid
c.execute("SELECT  rowid,* FROM customers")

#fetch data
items = c.fetchall()  #to fetch all the records
for item in items:   #looping through all records
    print(item)      #get all the items




#commit our command
conn.commit()
#close our connection
conn.close()