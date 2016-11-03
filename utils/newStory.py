import sqlite3

f = "test.db"

db = sqlite3.connect(f)
c = db.cursor()

def submit(post):
    if len(post) > 1000:
        return "post is too long, please resubmit"
    else:
        return "new post made"

