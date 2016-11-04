import sqlite3
#f = "test.db"
#db = sqlite3.connect(f)
#c = db.cursor()
#q = "CREATE TABLE posts (user TEXT, post_id INTEGER, story_id INTEGER, post TEXT)"
#c.execute(q)
#db.commit()
#db.close()


def submit(post):
    f = "test.db"

    db = sqlite3.connect(f)
    c = db.cursor()
    if len(post) > 1000:
        return "post is too long, please resubmit"
    else:
        text = '''"''' + post + '''"'''
        q = "INSERT INTO posts VALUES(%s, %i, %i, %s)" %('''"someone"''',0,0,text)
        c.execute(q)
        db.commit()
        db.close()
        return "post succesfully inputted"

   

