import database

# Add a record to the database
#database.add_one("Laura","Smith","laura@smith.com")

# Add Many Records
#stuff = [
#    ('Brenda','Smiter','brenda@smither.com'),
#    ('Josh','Rain','josh@rain.com')
#]
#database.add_many(stuff)

# Delete record use row id as 6
#database.delete_one('6')

# Show all records in the database
database.show_all()

# Lookup Email Address Record
#database.email_lookup("john@codemy.com")