import sqlite3

con = sqlite3.connect("studentregister.db")
print("Database opened successfully")

con.execute('''create table studentregisters(
            firstname TEXT,lastname TEXT,mailid TEXT,phonenum INTEGER,location TEXT,username TEXT,password TEXT
            )''')
con.commit()

print("Table created successfully")
con.close()
