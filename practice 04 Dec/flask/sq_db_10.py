#ordering results by
#oerding allows us to return the results in how we want
#delete a record
#delting is similar to updating
import sqlite3

conn = sqlite3.connect('customer.db')
c = conn.cursor()

#order By  asceding it prints
c.execute("SELECT rowid,* FROM customers ORDER BY rowid")
#order By  desceding it prints
c.execute("SELECT rowid,* FROM customers ORDER BY rowid DESC")
#order by last_name asending
c.execute("SELECT rowid,* FROM customers ORDER BY last_name")

items = c.fetchall() 

for item in items:
    print(item)
