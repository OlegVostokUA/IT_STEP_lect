import sqlite3

conn = sqlite3.connect('blog_database.db')

with open('shema.sql') as f:
    conn.executescript(f.read())

cur = conn.cursor()

cur.execute("""INSERT INTO posts (title, content) VALUES (?, ?)""",
            ('First post', 'content for first post'))

cur.execute("""INSERT INTO posts (title, content) VALUES (?, ?)""",
            ('Second post', 'content for second post'))

conn.commit()

conn.close()