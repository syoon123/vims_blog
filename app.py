from flask import Flask, render_template, request, url_for, session, redirect
import hashlib, sqlite3
from utils import contribute

f="storymaker.db"

#db = sqlite3.connect(f) #open if f exists, otherwise create
#c = db.cursor()    #facilitate db ops

#table already created, debug w/out

# #Initializing Tables: should be executed once (?)
# q = "CREATE TABLE user (user TEXT, pass TEXT)"
# c.execute(q)
#
# q = "CREATE TABLE posts (user TEXT, pid INTEGER, sid INTEGER, content TEXT)"
# c.execute(q)
#
# #test data
# q = "INSERT INTO user VALUES(\'mcVans\', \'vanna\')"
# c.execute(q)
# q = "INSERT INTO user VALUES(\'mcKissy\', \'issac\')"
# c.execute(q)
# q = "INSERT INTO user VALUES(\'mcCow\', \'michael\')"
# c.execute(q)
# q = "INSERT INTO user VALUES(\'mcYoonibrow\', \'sarah\')"
# c.execute(q)
#
# q = "INSERT INTO posts VALUES(\'mcVans\', 0,0,\'hello\')"
# c.execute(q)
# q = "INSERT INTO posts VALUES(\'mcKissy\', 1,0,\'my\')"
# c.execute(q)
# q = "INSERT INTO posts VALUES(\'mcCow\', 1,1,\'name\')"
# c.execute(q)
# q = "INSERT INTO posts VALUES(\'mcYoonibrow\', 2,0,\'is\')"
# c.execute(q)

app = Flask(__name__)
app.secret_key = '<j\x9ch\x80+\x0b\xd2\xb6\n\xf7\x9dj\xb8\x0fmrO\xce\xcd\x19\xd49\xe5S\x1f^\x8d\xb8"\x89Z'

def register(username, password):
    #check if requested username is in TABLE user of database
    return "You are already registered."
    #else write in new entry into database (hash pass)
    return "You are now successfully registered."

def checkLogin(username,password):
    hash = hashlib.sha1(password).hexdigest()
    ## check database if user-pass is correct
    #  if correct login -> return ""
    #  if no such username -> return "Incorrect Username"
    #  if incorrect pass -> return "Incorrect password!"

@app.route("/")
@app.route("/homepage/")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("homepageTemplate.html")

@app.route("/login/")
def login():
    if "user" in session:
        return redirect(url_for("/"))
    return render_template("loginTemplate.html", status = "")

#is there a way get rid of /authentication/ and just have everything in /login/ ?
@app.route("/authentication/", methods = ["GET", "POST"])  #idk which it should be
def authentication():
    if request.form["enter"] == "Register":
        register_message = register(request.form["user"],request.form["pass"])
        return render_template("loginTemplate.html", status = register_message)
    if request.form["enter"] == "Login":
        session["user"] = request.form["user"]
        #login_message = checkLogin(request.form["user"],request.form["pass"])

        ##if correct login -> homepage
        return render_template("homepageTemplate.html")

        ##if incorrect login -> /login/   status = loginMsg

@app.route("/logout/")
def logout():
    session.pop("user")
    return redirect(url_for("login"))

@app.route('/contribute/<int:storyid>')
def add(storyid):
    return contribute.addToStory(storyid)

@app.route('/addtoDB/', methods=['POST'])
def addtoDB():
    storyid = request.form['sid']
    content = request.form['newText']

    db = sqlite3.connect(f)
    c = db.cursor()

    #add to proper story by proper user
    p = 0
    cmd = "INSERT INTO posts VALUES(" + "'" + session['user'] + "'" + "," + "'" + str(p) + "'" + "," + "'" + str(storyid) + "'" + "," + "'" + content + "')"

    c.execute(cmd)

    db.commit()
    db.close()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.debug = True
    app.run()
