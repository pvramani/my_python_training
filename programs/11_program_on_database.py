"""
Get the data from the db
"""

print("Get the data from the db")
print("-"*20)
# -----------

import sqlite3

print("Create/Connect to database 'my_database.sqlite3'")
my_db_connection = sqlite3.connect("my_database.sqlite3")
print("Done\n\n")

print("Create cursor object")
my_db_cursor = my_db_connection.cursor()
print("Done\n\n")

print("Execute select query")
my_query = "SELECT * FROM MY_TABLE"
my_db_cursor.execute(my_query)
print("Done\n\n")

print("Get data from cursor")
my_db_result = my_db_cursor.fetchall()
print("Done\n\n")

print(my_db_result)

print("#"*40, end="\n\n")
# ###############################