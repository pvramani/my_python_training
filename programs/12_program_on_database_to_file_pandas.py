# pip install openpyxl
# pip install lxml
"""
Get data from database
and write to below files
db_dump_1.txt
db_dump_2.csv
db_dump_3.xlsx
db_dump_4.json
db_dump_5.xml
"""

print("Get the data from the db")
print("-"*20)
# -----------

import sqlite3

print("Create/Connect to database 'my_database.sqlite3'")
my_db_connection = sqlite3.connect("my_database.sqlite3")
print("Done\n\n")

import pandas as pd

my_db_data_df = pd.read_sql("SELECT * FROM MY_TABLE", my_db_connection)
print(my_db_data_df)

print("#"*40, end="\n\n")
# ###############################

print("Write to files")
print("-"*20)
# -----------

my_db_data_df.to_csv("db_dump_1.txt", sep="\t")
my_db_data_df.to_csv("db_dump_2.csv") # default sep=","
my_db_data_df.to_excel("db_dump_3.xlsx", sheet_name="my_db_data")
my_db_data_df.to_json("db_dump_4.json")
my_db_data_df.to_xml("db_dump_5.xml")

print("""
Below files are created. 
db_dump_1.txt
db_dump_2.csv
db_dump_3.xlsx
db_dump_4.json
db_dump_5.xml
Please check""")

print("#"*40, end="\n\n")
# ###############################