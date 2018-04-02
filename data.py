import sqlite3
with sqlite3.connect("database1.db") as db:
    cursor = db.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
name VARCHAR(20) NOT NULL,
mobile INTEGER PRIMARY KEY NOT NULL,
email NOT NULL,
address VARCHAR(50) NOT NULL,
password  NOT NULL);
''')    

db.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
    
