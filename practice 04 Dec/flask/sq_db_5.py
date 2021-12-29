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
c.execute("SELECT * FROM customers")
# print(c.fetchone()[0])   #to get first item in tuple
#print(c.fetchall())   #fetches all doesn't return anything so use print returns in list

items=c.fetchall()
print("name"+"\t\t"+"second name"+"\t\t"+"email")
for item in items:
    print(item[0] +"\t\t"+item[1]+"\t\t"+item[2])

#commit our command
conn.commit()
#close our connection
conn.close()
