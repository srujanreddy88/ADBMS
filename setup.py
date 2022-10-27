import sqlite3

# DB-API spec for talking to relational databases in Python

connection = sqlite3.connect("Vehicles.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table list")
except:
    pass

cursor.execute("create table list (id integer primary key, description text)")

cursor.execute("insert into list (description) values ('cars')")
cursor.execute("insert into list (description) values ('bikes')")
cursor.execute("insert into list (description) values ('trucks')")
cursor.execute("insert into list (description) values ('buses')")


connection.commit()
connection.close()

print("done.")