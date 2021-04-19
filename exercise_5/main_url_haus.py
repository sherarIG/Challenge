"""
This program will connect to an API from URLHAUS, download all the malware urls listed. It will create a dictionary
with those urls and finally with the data create:
- A json file
- A csv file
- An XML file
- An SQLite database (parameter), a table (parameter) and store the data in the mentioned table.
The dictionary structure is {id: , url:} where id is a unique incremental value.
The program uses two modules: sql_admin.py that handles the interactions with the database and file_admin.py that handles the creation of each of the files

PARAMETERS:
    db_name str : name for the database that the program will create
    table_name str : name for the table that the program will create inside the database

"""
import requests
from sql_admin import create_connection, create_table, add_record
from file_admin import generate_json, generate_csv, generate_xml
import os

# PARAMETERS
db_name = 'urlhaus'
table_name = 'taUrlHaus'
# DICTIONARY WHERE WE ARE GOING TO STORE THE URLs
urls_dict = {}
# MAKE THE REQUEST TO THE API
try:
    r = requests.get('https://urlhaus.abuse.ch/downloads/text/')
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

# SPLIT THE LINES INTO A LIST BASED ON NEW LINE CHARACTER "\n"
lines = r.text.split("\n")
i = 1
for line in lines:
    # ONLY STORE THE LINES THAT START WITH 'http'
    if line[0:4] == 'http':
        # DEFINE AND id FOR EACH OF THE URLS (i)
        urls_dict[str(i)] = line
        i += 1

# CREATE JSON, CSV and XML files
json_file = generate_json(urls_dict)
csv_file = generate_csv(urls_dict)
xlm_file = generate_xml(urls_dict)

# CREATE SQLite DB CONNECTION
db_filename = os.path.abspath(os.getcwd()) + '/' + db_name + ".db"
conn = create_connection(db_filename)

# CREATE TABLE AND ADD RECORDS
if conn is not None:
    create_table(conn, table_name)
    for key, value in urls_dict.items():
        last_row_id = add_record(conn, table_name, [key, value])
    conn.commit()
    conn.close()
