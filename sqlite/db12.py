# and and or in where class
import sqlite3
#to cteate connection
conn = sqlite3.connect("customers.db")
#create cursor tells what db to do
c=conn.cursor()

# #last name is strats with k
# c.execute("SELECT rowid,* FROM customers WHERE last_name LIKE 'k%'")
# #2 conditions
# c.execute("SELECT rowid,* FROM customers WHERE last_name LIKE 'k%' AND rowid=1")
#or condition
c.execute("SELECT rowid,* FROM customers WHERE last_name LIKE 'k%' OR rowid=1")


items=c.fetchall()

for item in items:
    print(item)

#commit our command
conn.commit()
#close our connection
conn.close()