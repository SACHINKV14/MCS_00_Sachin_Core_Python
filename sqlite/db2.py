#create a db table
import sqlite3

#to cteate connection to save our database
conn = sqlite3.connect("customers.db") #creates db

#create cursor tells what db to do
c=conn.cursor()

#create a table
c.execute("""CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
    )""")

#datatypes
# Null (doesnt exist)
# Integer(whloe number)
#real(decimal)
#text(text)
#blob(stores exaxtly as it is)

#commit our command
conn.commit()

#close our connection
conn.close()

