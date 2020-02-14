import sqlite3

conn = sqlite3.connect('tracksdb.sqlite')
cur = conn.cursor()

cur.execute('Select * from Artist where id = ?', (10000,))
data = cur.fetchone()
print(data)
