#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO THURSDAY (ID,BAND,HOMETOWN,YEAR) VALUES (1, 'The Beathes', 'Liverpool, England', 1960 )")

conn.execute("INSERT INTO THURSDAY (ID,BAND,HOMETOWN,YEAR) VALUES (2, 'Guns and Roses', 'Los Angeles, USA', 1985 )")

conn.execute("INSERT INTO THURSDAY (ID,BAND,HOMETOWN,YEAR) VALUES (3, 'Agnee', 'Pune, India', 2007 )")

conn.commit()
print("Records created successfully")
conn.close()

