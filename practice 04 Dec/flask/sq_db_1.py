#import sqdatabase
import sqlite3
#create connection to db parameter name of the db
#if db not presents it creates a db
conn=sqlite3.connect('customer.db')

'''
it creates a db in memory as soon as we close the file db clears
conn=sqlite3.connect(':memory:')
'''

#create cursor
c=conn.cursor()

#create table
#doc string is 6 quotes inside this we can write multiple lines multiple things
#create table
#table name as customers
#define rows and columns
#with datatype define which type of data it is
c.execute("""CREATE TABLE customers (
    first_name text,  
    last_name text,
    email text 
)""")

'''data types
#null
#integer
#real
#text
#blob  is stores exaclty as it is img ,mp3
'''

#commiting our command to a db
conn.commit()
#close our connection
conn.close()