from flask import Flask, render_template, request, session, url_for
import sqlite3
#set proper template folder path
app = Flask(__name__, template_folder = '../templates')

def addToStory(storyid):

    #not logged in
    if 'user' not in session:
        #redirect(url_for('login'))
        return render_template('loginTemplate.html', status = "")

    else:

        f = 'storymaker.db'
        db = sqlite3.connect(f)
        c = db.cursor()
        q = "select user, sid from posts where sid == " + str(storyid)
        sel = c.execute(q)

        for record in sel:
            if record[0]==session['user']:
                post = ""
                t = ""
                q = "select title, content from posts where sid = " + str(storyid)
                alltext = c.execute(q)

                for piece in alltext:
                    t = piece[0]
                    post += " " + piece[1]                    

                return render_template('viewStory.html', text = post, title = t)

        #add new
        q = "select title from posts where sid = " + str(storyid)
        c.execute(q)
        out = c.fetchall()
        t = out[0][0]
        print("title:" + t)
        return render_template('contributeForm.html', id = storyid, storytitle = t)
