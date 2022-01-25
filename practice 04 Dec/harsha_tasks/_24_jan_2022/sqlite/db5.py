#Query and fetch all
import sqlite3
#to cteate connection
conn = sqlite3.connect("customers.db")
#create cursor tells what db to do
c=conn.cursor()

#query the database
c.execute("SELECT * FROM customers")

#fetch data
# c.fetchone()   #to fetch one
# c.fetchmany(3)  #to fetching many
print(c.fetchall())    #to fetch all the records

#commit our command
conn.commit()
#close our connection
conn.close()