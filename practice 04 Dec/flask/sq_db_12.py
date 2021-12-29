#limiting results
#when we large nuber of datas need to print certain number of datas
#AND & OR
# extends the functionalaties of where clause
#ordering results by
#oerding allows us to return the results in how we want
#delete a record
#delting is similar to updating
import sqlite3

conn = sqlite3.connect('customer.db')
c = conn.cursor()

#use limit
c.execute("SELECT rowid,* FROM customers ORDER BY rowid DESC LIMIT  2")

items = c.fetchall()
for item in items:
    print(item)
conn.commit()
conn.close()