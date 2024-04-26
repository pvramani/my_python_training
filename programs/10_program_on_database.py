"""
https://sqlitebrowser.org/dl/

Get data from sample_data.txt,
extract info using regular expression
send extracted data to database
"""

"""
How to communicate with database?

python-program  <--communicate using library--> Any Databases

Example:
python-program  <--communicate using library (cx-oracle)--> Oracle Databases
python-program  <--communicate using library (sqlite3)--> SQLite Databases
"""

"""
We need one database?
- we can use SQLite database

How to create/communicate with SQLite database?
OPTION-1: using sqlite database software
OPTION-2: using sqlite3 library we can create/communicate with SQLite database
            without using sqlite database software
"""

print("Get data from sample_data.txt")
print("-"*20)
# -----------

my_log_file_handle = open(r"../log/sample_data.txt", "r")
log_file_content = my_log_file_handle.readlines()
print(log_file_content)

print("#"*40, end="\n\n")
# ###############################

print("Create database and table")
print("-"*20)
# -----------

import sqlite3

print("Create/Connect to database 'my_database.sqlite3'")
my_db_connection = sqlite3.connect("my_database.sqlite3")
print("Done\n\n")

print("Create cursor object")
my_db_cursor = my_db_connection.cursor()
print("Done\n\n")

print("Create table if not present")
my_query = """
CREATE TABLE IF NOT EXISTS MY_TABLE(
IP VARCHAR(100),
DATE VARCHAR(100),
PICS VARCHAR(100),
URL VARCHAR(100)
)
"""
my_db_cursor.execute(my_query)

print("Done\n\n")


print("#"*40, end="\n\n")
# ###############################

print("Extract and write to database")
print("-"*20)
# -----------

import re

for each_line in log_file_content:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*?(GET|POST|PUT|PATCH|DELETE)\s+/(pics/(\w+\.(jpg|gif)))?.*(http[s]?://[a-zA-Z_0-9./]+).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        url = match_result.group(7)
        my_query = f"INSERT INTO MY_TABLE VALUES('{ip}', '{dt}', '{img}', '{url}')"
        print("Executing Query:",my_query)
        my_db_cursor.execute(my_query)
        print("One Record Inserted\n\n")

my_db_connection.commit()
print("All records inserted\n\n")

my_db_connection.close()
print("DB connection closed\n\n")

print("#"*40, end="\n\n")
# ###############################