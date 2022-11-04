import sqlite3
#sqlte3 uses Files for its databases. create it, if it doesn't exit
dbconnect=sqlite3.connect("demo")
#dbconnect.execute("""CREATE TABLE IF NOT EXISTS MOVIES
#        (
#        ID    INT  PRIMARY KEY NOT NULL,
#        TITLE TEXT  NOT NULL,
#        YEAR  INT   NOT NULL,
#        TYPE TEXT    NOT NULL);""")
#dbconnect.execute("INSERT INTO MOVIES (ID, TITLE, YEAR, TYPE) VALUES (1, 'Shrek', 2001, 'Movie')")
#dbconnect.execute("INSERT INTO MOVIES (ID, TITLE, YEAR, TYPE) VALUES (2, 'Shrek The Third', 2007, 'Movie')")
#dbconnect.commit()

cursor=dbconnect.execute("SELECT * FROM MOVIES")
for x in cursor:
    print(x)
    print(f"The {x[3].lower()} {x[1]} came out in {x[2]}!")


#always close files/connections
dbconnect.close()
