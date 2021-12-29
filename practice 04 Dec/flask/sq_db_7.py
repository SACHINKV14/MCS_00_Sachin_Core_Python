#where clause
#searching for specific things in database

#primary keys unique id number each record in a table gets
#format your results
#query and fetch all
#get from db and display it
import sqlite3
#connect to db
conn = sqlite3.connect('customer.db')
#create a cursor
c = conn.cursor()

#query the database
#* selects all

#where is used to find particular last_name is equal to elder
#we can use operators too if we numbers >,<,=<(logica )
c.execute("SELECT * FROM customers WHERE last_name='kv'")
'''
search for the name starts with Sa
c.execute("SELECT * FROM customers WHERE last_name LIKE 'Sa%")
search for the email  ends with codemy.com
c.execute("SELECT * FROM customers WHERE email LIKE '%codemy.com")
'''
# print(c.fetchone()[0])   #to get first item in tuple
#print(c.fetchall())   #fetches all doesn't return anything so use print returns in list

items=c.fetchall()
for item in items:
    print(item)




#commit our command
conn.commit()
#close our connection
conn.close()
