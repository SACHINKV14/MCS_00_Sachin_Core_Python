#insert many records into the table

import sqlite3
#connect to db
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()
#inside values need to use single quotes
many_customers = [ 
                    ('sa','k','sak@gmail.com'),
                    ('d','ms','msd@gmail.com'),
                    ('v','k','vk@gmail.com')
                ]
#instead of exceute use executemany
#use ? placeholders
c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)

#to see command
print("command executed successfully...")
#commit our command
conn.commit()
#close our connection
conn.close()

