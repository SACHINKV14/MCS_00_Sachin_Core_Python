#AND & OR
# extends the functionalaties of where clause
#ordering results by
#oerding allows us to return the results in how we want
#delete a record
#delting is similar to updating
import sqlite3

conn = sqlite3.connect('customer.db')
c = conn.cursor()

#AND(all of them is to be true) / OR(any one of them to be true)
c.execute("SELECT rowid,* FROM customers WHERE last_name LIKE 'k%' AND rowid =1")
#any one condition is true its print
c.execute("SELECT rowid,* FROM customers WHERE last_name LIKE 'k%' OR rowid =1")

items = c.fetchall()
for item in items:
    print(item)
conn.commit()
conn.close()