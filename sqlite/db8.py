#where clause(search for particulars)
#Query and fetch all
import sqlite3
#to cteate connection
conn = sqlite3.connect("customers.db")
#create cursor tells what db to do
c=conn.cursor()

#can use logical operators =,<,>
# c.execute("SELECT *From customers WHERE last_name='kv'")
#last starst with k ends with anything
# c.execute("SELECT *From customers WHERE last_name LIKE 'k%'")
#email like
c.execute("SELECT *From customers WHERE email LIKE '%rcb.com'")

items =c.fetchall()
for item in items:
    print(item)




#commit our command
conn.commit()
#close our connection
conn.close()
