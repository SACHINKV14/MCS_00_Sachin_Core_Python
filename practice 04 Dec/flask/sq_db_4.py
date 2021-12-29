#query and fetch all
#get from db and display it
import sqlite3
#connect to db
conn = sqlite3.connect('customer.db')
#create a cursor
c = conn.cursor()

#query the database
#* selects all
c.execute("SELECT * FROM customers")
# c.fetchone()  #fetches the last item in table
# c.fetchmany()  #fetches many
print(c.fetchall())   #fetches all doesn't return anything so use print returns in list

#to see command
# print("command executed successfully...")
#commit our command
conn.commit()
#close our connection
conn.close()
