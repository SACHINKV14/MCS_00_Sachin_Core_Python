#update records

import sqlite3
#to cteate connection
conn = sqlite3.connect("customers.db")
#create cursor tells what db to do
c=conn.cursor()

#update records
#changes all the names where last name is kv
# c.execute("""UPDATE customers SET first_name='Sachin'
#     where last_name='kv'
#
#             """)

#updating based on rowid
c.execute("""UPDATE customers SET first_name='Sachinn'
    where rowid=2

            """)


#commit our command
conn.commit()

c.execute("SELECT rowid,* FROM customers")

#fetch data
items = c.fetchall()  #to fetch all the records
for item in items:   #looping through all records
    print(item)      #get all the items


#close our connection
conn.close()