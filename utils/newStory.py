import sqlite3



def submit(post):
    f = "test.db"

    db = sqlite3.connect(f)
    c = db.cursor()
    if len(post) > 1000:
        return "post is too long, please resubmit"
    else:
        q = "INSERT INTO posts VALUES(%s, %i, %i, %s)" %("someone",1,1,post)
        c.execute(q)

    db.commit()
    db.close()

