#Order Results By
import sqlite3
#to cteate connection
conn = sqlite3.connect("customers.db")
#create cursor tells what db to do
c=conn.cursor()

#order by
# #ascending order
# c.execute("SELECT rowid,* FROM customers ORDER BY rowid")

# #descedning order
# c.execute("SELECT rowid,* FROM customers ORDER BY rowid DESC")

# #orde by last name
# c.execute("SELECT rowid,* FROM customers ORDER BY last_name")
#orde by last name
c.execute("SELECT rowid,* FROM customers ORDER BY last_name DESc")



items=c.fetchall()

for item in items:
    print(item)




#commit our command
conn.commit()
#close our connection
conn.close()