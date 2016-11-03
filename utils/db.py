import sqlite3

f = "test.db"

db = sqlite3.connect(f)
c = db.cursor()

q = "CREATE TABLE posts (user TEXT, post_id INTEGER, story_id INTEGER, post TEXT)"
c.execute(q)

db.commit()
db.close()
