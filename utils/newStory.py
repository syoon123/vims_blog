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
    cmd = "SELECT story_id FROM posts WHERE post_id = 0;"
    stories = c.execute(cmd)
    i = 0
    for story in stories:
        i = i + 1
    db.close()
    return i
    
def submit(post):
    f = "test.db"
    story_id = getID()
    db = sqlite3.connect(f)
    c = db.cursor()
    if len(post) > 1000:
        return "post is too long, please resubmit"
    else:
        text = '''"''' + post + '''"'''
        q = "INSERT INTO posts VALUES(%s, %i, %i, %s)" %('''"someone"''',0,story_id,text)
        c.execute(q)
        db.commit()
        db.close()
        return "post succesfully inputted"


   

