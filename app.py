from flask import Flask, render_template, request, url_for, session, redirect
import hashlib, sqlite3
from utils import contribute, newStory

f="storymaker.db"

app = Flask(__name__)
app.secret_key = '<j\x9ch\x80+\x0b\xd2\xb6\n\xf7\x9dj\xb8\x0fmrO\xce\xcd\x19\xd49\xe5S\x1f^\x8d\xb8"\x89Z'

def register(username, password):
    db = sqlite3.connect(f)
    c = db.cursor()
    query = "SELECT user FROM users"
    dbUsers = c.execute(query)

    for entry in dbUsers:
        if (entry[0] == username):
            return "You are already registered."  #check if username is taken

    hashedPass = hashlib.sha1(password).hexdigest()
    insertQuery = "INSERT INTO users VALUES(\'%s\',\'%s\')"%(username,hashedPass)

    c = db.cursor()
    c.execute(insertQuery)

    db.commit()
    db.close()
    return "You are now successfully registered."

def checkLogin(username,password):
    hashedPass = hashlib.sha1(password).hexdigest()
    db = sqlite3.connect(f)
    c = db.cursor()
    query = "SELECT * FROM users"
    dbUserPass = c.execute(query)
    for entry in dbUserPass:
        if (entry[0] == username):
            if (entry[1] == hashedPass): return ""
            else: return "Incorrect Password"
    return "Incorrect Username"

@app.route("/")
@app.route("/homepage/")
def home():
    if "user" not in session:
        return redirect(url_for("login"))

    #get links to stories
    linkStr = ""
    allStoryStr = ""

    db = sqlite3.connect(f)
    c = db.cursor()
    query = "select sid from posts where user = " + session['user']
    try:
        storyHistory = c.execute(query)
    #if you have no stories?
    except:
        storyHistory = ""

    for entry in storyHistory:
        linkStr+= "<a href = '%s'></a><br>"%(entry[0])

    query = "SELECT sid FROM posts"
    allStories = c.execute(query)
    allStoryStr += "<center>"

    for entry in allStories:
        allStoryStr+= "<a href = '/contribute/%s'>%s</a><br>"%(entry[0],entry[0])

    allStoryStr += "</center>"

    return render_template("homepageTemplate.html", storyHistory = linkStr, allStories = allStoryStr)

@app.route("/login/", methods = ["GET","POST"])
def login():
    if "user" in session:
        return redirect(url_for("home"))
    if request.method == "GET":
        return render_template("loginTemplate.html", status = "")
    if request.form["enter"] == "Register":
        register_message = register(request.form["user"],request.form["pass"])
        return render_template("loginTemplate.html", status = register_message)
    if request.form["enter"] == "Login":
        login_message = checkLogin(request.form["user"],request.form["pass"])
        if (login_message == ""):
            session["user"] = request.form["user"]
            return redirect(url_for("home"))
        return render_template("loginTemplate.html", status = login_message)

@app.route("/logout/")
def logout():
    session.pop("user")
    return redirect(url_for("login"))

@app.route("/newstory/")
def post():
    return render_template("make_post.html")

@app.route("/postResult/", methods = ['POST'])
def result():
    r = request.form
    post = r['post']
    user = session['user']
    newStory.submit(post, user)
    return redirect(url_for('home'))

@app.route('/contribute/<int:storyid>')
def add(storyid):
    return contribute.addToStory(storyid)

@app.route('/addtoDB/', methods=['POST'])
def addtoDB():
    storyid = request.form['sid']
    content = request.form['newText']

    #deal w/apostrophes
    content = content.replace("'","''")

    db = sqlite3.connect(f)
    c = db.cursor()

    #add to proper story by proper user
    p = 0
    cmd = "INSERT INTO posts VALUES(" + "'" + session['user'] + "'" + "," + "'" + str(p) + "'" + "," + "'" + str(storyid) + "'" + "," + "'" + content + "')" #%(session['user'],str(p),str(storyid),content)
    c.execute(cmd)

    db.commit()
    db.close()
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.debug = True
    app.run()
