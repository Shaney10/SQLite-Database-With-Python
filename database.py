import sqlite3


# Query the database and return all records
def show_all():
    # Connect to Database and create cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    # Query the Database
    c.execute("SELECT rowid,* FROM Customers")
    items = c.fetchall()
    
    for item in items:
        print(item)

    # Commit command database
    conn.commit()
    # Close connection
    conn.close()

# Add a new record to the table
def add_one(first,last,email):
    # Connect to Database and create cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

    # Commit command database
    conn.commit()
    # Close connection
    conn.close()

def add_many(list):
    # Connect to Database and create cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))

    # Commit command database
    conn.commit()
    # Close connection
    conn.close()


 # Delete Record from the table
def delete_one(id):
    # Connect to Database and create cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", id)
    # Commit command database
    conn.commit()
    # Close connection
    conn.close()

# Lookup and Where
def email_lookup(email):
    # Connect to Database and create cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    # Query the Database
    c.execute("SELECT rowid, * FROM Customers WHERE email = (?)",(email,))
    items = c.fetchall()
    
    for item in items:
        print(item)

    # Commit command database
    conn.commit()
    # Close connection
    conn.close()


# Create Connection to Memery
#conn = sqlite3.connect(':memory:')

# Create Connection to Database and will create new if does not exist
#conn = sqlite3.connect('customer.db')

# Use Gitbash and set directory to path of .py file
# cd /c/Users/seanh/OneDrive/Desktop/SQLite3_Training
# ls
# database.py

# run database.py file 
# python database.py
# ls will now show .db file

# Build a table

# Create a cursor
#c = conn.cursor()

# Differnt data types :
# NULL
# INTEGER
# TEXT
# BLOB

# Create a Table using doc strings """
#c.execute("""CREATE TABLE customers (
#        first_name text,
#        last_name text,
#        email text
#    )""")

# Insert one value at a time into table
#c.execute("INSERT INTO customers VALUES ('John','Elder','john@codemy.com')")
#c.execute("INSERT INTO customers VALUES ('Tim','Smith','tim@codemy.com')")
#c.execute("INSERT INTO customers VALUES ('Mary','Brown','mary@codemy.com')")

# Insert many by creating a python list
#many_customers = [
#                    ('Wes', 'Brown', 'wes@brown.com'),
#                    ('Steph', 'Kuewa', 'steph@Kuewa.com'),
#                    ('Dan', 'Pas', 'dan@pas.com'),                
#                ]
#c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# Update Records
#c.execute("""UPDATE customers SET first_name = 'John'
#            WHERE rowid = 1
#     """)

# Delete Records
#c.execute("DELETE from customers WHERE rowid =6")

# Delete Table
#c.execute("DROP TABLE customers")

# Query the Database add rowid
#c.execute("SELECT * FROM Customers")
# Add rowid
#c.execute("SELECT rowid,* FROM Customers")
# Using WHERE
#c.execute("SELECT * FROM Customers WHERE last_name = 'Elder'")
# Using WHERE and LIKE
#c.execute("SELECT * FROM Customers WHERE email LIKE '%codemy.com'")

# Query the Database - Order by ASC DESC
#c.execute("SELECT rowid,* FROM Customers ORDER BY rowid DESC")
#c.execute("SELECT rowid,* FROM Customers ORDER BY last_name")

# Query the Database - AND/OR
#c.execute("SELECT rowid,* FROM Customers WHERE last_name LIKE 'Br%' AND rowid = 3")
#c.execute("SELECT rowid,* FROM Customers WHERE last_name LIKE 'Br%' OR rowid = 3")

# Query the Database - Order by ASC DESC with Limit
#c.execute("SELECT rowid,* FROM Customers ORDER BY rowid DESC LIMIT 2")

#c.fetchone
#c.fetchmany(3)
#c.fetchall()

# Put in a print statement to print
#print(c.fetchall())

# Create variable to loop through
#print("NAME " + "\t\tEmail")
#print ("-----" + "\t\t -----")
#items = c.fetchall()


#for item in items:
#    print(item)
#    print(item[0] + " " + item[1] + "\t" + item[2])

# Using unique row ID add row id after SELECT
#for item in items:
#    print(item)



#print("Command executed sucesfully...")

# Commit command database
#conn.commit()

# Close connection
#conn.close()



