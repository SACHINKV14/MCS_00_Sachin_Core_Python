#delete a record
#delting is similar to updating
import sqlite3

conn = sqlite3.connect('customer.db')
c = conn.cursor()

#for deleting 2nd record it is permananet delete
c.execute("DELETE from customers WHERE rowid = 2")


conn.commit()

c.execute("SELECT rowid,* FROM customers")

items = c.fetchall()

for item in items:
    print(item)
