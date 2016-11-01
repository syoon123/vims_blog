from flask import Flask, render_template, request, url_for, session, redirect
import hashlib
import sqlite3

f="storymaker.db"

app = Flask(__name__)
app.secret_key = '<j\x9ch\x80+\x0b\xd2\xb6\n\xf7\x9dj\xb8\x0fmrO\xce\xcd\x19\xd49\xe5S\x1f^\x8d\xb8"\x89Z'

def register(username, password):
    #check if already registered in database
            return "You are already registered."
    #else write in new entry into database
    return "You are now successfully registered."

#def checkLogin(username,password):
    #passFileReader = csv.reader(open(passFile))
    #for i in passFileReader:
    #    if username == i[0]:
    #        if i[1] == hashlib.sha1(password).hexdigest():
    #            return "You are logged in."
    #        return "Incorrect password!"
    #return "No such username"


@app.route("/")
@app.route("/homepage")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("homepageTemplate.html")

@app.route("/login/")
def login():
    if "user" in session:  
        return redirect(url_for("/"))
    return render_template("loginTemplate.html", status = "")

@app.route("/authentication/", methods = ["GET", "POST"])
def authentication():
    if request.form["enter"] == "Register":
        register_message = register(request.form["user"],request.form["pass"])
        return render_template("authentication.html", status = register_message)
    if request.form["enter"] == "Login":
        session["user"] = request.form["user"] #cookie
        #login_message = checkLogin(request.form["user"],request.form["pass"])
        
        ##if correct login -> homepage
        return render_template("homepageTemplate.html")

        ##if incorrect login -> /login/   status = loginMsg

@app.route("/logout/")    
def logout():
    session.pop("user")
    return redirect(url_for("login"))
        
if __name__ == "__main__":
    app.debug = True
    app.run()