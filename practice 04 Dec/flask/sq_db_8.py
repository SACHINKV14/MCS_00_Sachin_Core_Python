#update records
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

#update records

#setting first name where last name is k
#it will change the all the records which have last name k

# c.execute("""UPDATE customers SET first_name = 'Sachin'
#             WHERE last_name = 'k'
#     """)

#using rowid setiing the first name
c.execute("""UPDATE customers SET first_name = 'Virat'
            WHERE rowid = 6
    """)
#commit this
conn.commit()





#query the database
c.execute("SELECT rowid,* FROM customers")


items=c.fetchall()
for item in items:
    print(item)




#commit our command
conn.commit()
#close our connection
conn.close()
