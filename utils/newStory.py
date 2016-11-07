import sqlite3
#f = "test.db"
#db = sqlite3.connect(f)
#c = db.cursor()
#q = "CREATE TABLE posts (user TEXT, post_id INTEGER, story_id INTEGER, post TEXT)"
#c.execute(q)
#db.commit()
#db.close()

def getID():
    f = "storymaker.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    cmd = "SELECT sid FROM posts WHERE pid = 0;"
    stories = c.execute(cmd)
    i = 0
    for story in stories:
        i = i + 1
    db.close()
    return i
    
def submit(title, post, username):
    f = "storymaker.db"
    story_id = getID()
    db = sqlite3.connect(f)
    c = db.cursor()
    text = '''"''' + post + '''"'''
    user = '''"''' + username + '''"'''
    t = '''"''' + title + '''"'''
    q = "INSERT INTO posts VALUES(%s, %i, %i, %s, %s)" %(user,0,story_id,t,text)
    c.execute(q)
    db.commit()
    db.close()
