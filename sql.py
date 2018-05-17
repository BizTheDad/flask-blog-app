import sqlite3
from config import DB_PATH

with sqlite3.connect(DB_PATH) as connection:
    c = connection.cursor()

    c.execute("CREATE TABLE posts(title TEXT, post TEXT)")

    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
    c.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
    c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')
