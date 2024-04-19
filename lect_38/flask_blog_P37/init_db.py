import sqlite3

conn = sqlite3.connect('blog_db.db')

with open('shema.sql') as f:
    conn.executescript(f.read())

cur = conn.cursor()

cur.execute("""INSERT INTO posts (title, content) VALUES (?, ?)""", ('First post', 'Text for first post, text for first post'))

cur.execute("""INSERT INTO posts (title, content) VALUES (?, ?)""", ('Second post', 'Text for second post, text for second post'))

conn.commit()

conn.close()