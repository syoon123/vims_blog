import sqlite3
#f = "test.db"
#db = sqlite3.connect(f)
#c = db.cursor()
#q = "CREATE TABLE posts (user TEXT, post_id INTEGER, story_id INTEGER, post TEXT)"
#c.execute(q)
#db.commit()
#db.close()

def getID():
    f = "test.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    cmd = "SELECT * FROM posts WHERE post_id = 0;"
    stories = c.execute(cmd)
    db.close()
    return len(stories)
    
def submit(post):
    f = "test.db"
    story_id = getID()
    db = sqlite3.connect(f)
    c = db.cursor()
    if len(post) > 1000:
        return "post is too long, please resubmit"
    else:
        text = '''"''' + post + '''"'''
        q = "INSERT INTO posts VALUES(%s, %i, %i, %s)" %('''"someone"''',story_id,0,text)
        c.execute(q)
        db.commit()
        db.close()
        return "post succesfully inputted"

print(getID())
   

