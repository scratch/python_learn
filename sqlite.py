import sqlite3

conn = sqlite3.connect ('emaidb.sqlite')
cur = conn.cursor()
conn.close();
