#insert many records into database

import sqlite3

#to cteate connection
conn = sqlite3.connect("customers.db")

#create cursor tells what db to do
c=conn.cursor()

many_customers=[('abd','rcb','abd@rcb.com'),
               ('maxi','rcb','maxi@rcb.com'),
               ('gayle','rcb','gayle@rcb.com')
              ]
#Insert data into table
c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)


print("command executed succesfully...")
#commit our command
conn.commit()

#close our connection
conn.close()