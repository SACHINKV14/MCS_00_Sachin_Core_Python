import database

#add a record to the database
database.add_one("sac","k","sack@gmail.com")
# add many records to the database
stuff=[
    ('van','v','vanv@gmail.com'),
    ('can','v','canv@gmail.com')
]
database.add_many(stuff)

# lookup email address record
database.email_lookup("john@gmail.com ")
#delete one record
#here id should be passed as string not an integer
database.delete_one('6')

#to showw all the records
database.show_all()