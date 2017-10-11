#!/usr/bin/python
import sqlite3

conn = sqlite3.connect('scores.db')
print("[Database] Opened scores.db")

conn.execute('''CREATE TABLE SCORES
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       SCORE            INT     NOT NULL);''')
print("[Database] Created tables")

conn.close()
print("[Database] Closed scores.db")

print("[Database] Initialisation completed")
