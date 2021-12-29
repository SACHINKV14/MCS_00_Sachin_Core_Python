#primary keys unique id number each record in a table gets
#format your results
#query and fetch all
#get from db and display it
import sqlite3
#connect to db
conn = sqlite3.connect('customer.db')
#create a cursor
c = conn.cursor()

#query the database
#* selects all

#rowid is unique id for each record
c.execute("SELECT rowid, * FROM customers")
# print(c.fetchone()[0])   #to get first item in tuple
#print(c.fetchall())   #fetches all doesn't return anything so use print returns in list

items=c.fetchall()
for item in items:
    print(item)




#commit our command
conn.commit()
#close our connection
conn.close()