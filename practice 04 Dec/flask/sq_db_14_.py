#data base APP(Show all functions)
import sqlite3
#query the DB and return all records
def show_all():
    #connect to database
    conn = sqlite3.connect('customer.db')
    #create a cursor
    c = conn.cursor()
    #query the database
    c.execute("SELECT rowid,* FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)
    #commit our command
    conn.commit()
    #close our connection
    conn.close()

#Add a new record to the table
def add_one(first,last,email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)",(first,last,email))
    # commit our command
    conn.commit()
    # close our connection
    conn.close()
#add many records to table
def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (list))
    # commit our command
    conn.commit()
    # close our connection
    conn.close()

#lookup with where
def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid,* from customers WHERE eail = (?)",(email,))
    items = c.fetchall()
    for item in items:
        print(item)
    # commit our command
    conn.commit()
    # close our connection
    conn.close()



#Delete record from table
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERErowid = (?)", id)
    conn.commit()
    conn.close()


