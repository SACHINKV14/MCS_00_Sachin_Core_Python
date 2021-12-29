#delete(drop) a table
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
#drop table
c.execute("DROP TABLE customers")
conn.commit()
#gives error bcz its deleted 
c.execute("SELECT rowid,* FROM customers")

items = c.fetchall()
for item in items:
    print(item)
conn.commit()
conn.close()
