#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
conn.execute('''CREATE TABLE THURSDAY
 (ID INT PRIMARY KEY     NOT NULL,
 BAND           TEXT    NOT NULL,
 HOMETOWN       TEXT     NOT NULL,
 YEAR           INT NOT NULL);''')
print("Table created successfully")
conn.close()

