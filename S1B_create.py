# (A) LOAD PACKAGES
import sqlite3, os
from sqlite3 import Error

# (B) DATABASE + SQL FILE
DBFILE = "DB\\events2.db"
SQLFILE = "SQLs\\S1A_events.sql"

# (C) DELETE OLD DATABASE IF EXISTS
if os.path.exists(DBFILE):
    os.remove(DBFILE)

# (D) IMPORT SQL
conn = sqlite3.connect(DBFILE)
with open(SQLFILE) as f:
    conn.executescript(f.read())
conn.commit()
conn.close()
print("Database created")
