import hashlib,sqlite3

f="storymaker.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

q = "CREATE TABLE users (user TEXT, pass TEXT)"
c.execute(q)

'''
q = "INSERT INTO users VALUES(\'mcVans\', \'%s\')" %(hashlib.sha1("vanna").hexdigest())
c.execute(q)
q = "INSERT INTO users VALUES(\'mcKissy\', \'%s\')"%(hashlib.sha1("issac").hexdigest())
c.execute(q)
q = "INSERT INTO users VALUES(\'mcCow\', \'%s\')"%(hashlib.sha1("michael").hexdigest())
c.execute(q)
q = "INSERT INTO users VALUES(\'mcYoonibrow\', \'%s\')"%(hashlib.sha1("sarah").hexdigest())
c.execute(q)
'''

q = "CREATE TABLE posts (user TEXT, pid INTEGER, sid INTEGER, title TEXT, content TEXT)"
c.execute(q)

'''
q = "INSERT INTO posts VALUES(\'mcVans\', 0,0,\'hello\')"
c.execute(q)
q = "INSERT INTO posts VALUES(\'mcKissy\', 1,0,\'my\')"
c.execute(q)
q = "INSERT INTO posts VALUES(\'mcCow\', 1,1,\'name\')"
c.execute(q)
q = "INSERT INTO posts VALUES(\'mcYoonibrow\', 2,0,\'is\')"
c.execute(q)
'''

db.commit() #save changes
db.close()  #close database
