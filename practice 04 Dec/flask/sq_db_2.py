#insert one record into a db
import sqlite3
#connect to db
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()
#inside values need to use single quotes
c.execute("INSERT INTO customers VALUES ('dhoni','ms','dhoni07@gmail.com')")

#to see command
print("command executed successfully...")
#commit our command
conn.commit()
#close our connection
conn.close()
