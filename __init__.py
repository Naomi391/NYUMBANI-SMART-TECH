import sqlite3

CONN = sqlite3.connect('realestate.db')
CURSOR = CONN.cursor()

CONN.commit()
CURSOR.close()
CONN.close()