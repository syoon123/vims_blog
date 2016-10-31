import sqlite3

f="storymaker.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

q = "CREATE TABLE user (user TEXT, pass TEXT)"
c.execute(q)

q = "INSERT INTO user VALUES(\'mcVans\', \'vanna\')"
c.execute(q)
q = "INSERT INTO user VALUES(\'mcKissy\', \'issac\')"
c.execute(q)
q = "INSERT INTO user VALUES(\'mcCow\', \'michael\')"
c.execute(q)
q = "INSERT INTO user VALUES(\'mcYoonibrow\', \'sarah\')"
c.execute(q)

q = "CREATE TABLE posts (user TEXT, pid INTEGER, sid INTEGER, content TEXT)"
c.execute(q)

q = "INSERT INTO posts VALUES(\'mcVans\', 0,0,\'hello\')"
c.execute(q)
q = "INSERT INTO posts VALUES(\'mcKissy\', 1,0,\'my\')"
c.execute(q)
q = "INSERT INTO posts VALUES(\'mcCow\', 1,1,\'name\')"
c.execute(q)
q = "INSERT INTO posts VALUES(\'mcYoonibrow\', 2,0,\'is\')"
c.execute(q)

db.commit() #save changes
db.close()  #close database
