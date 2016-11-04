from flask import Flask, render_template, request, session, url_for
import sqlite3
#set proper template folder path
app = Flask(__name__, template_folder = '../templates')

def addToStory(storyid):
    if 'user' not in session:
        #redirect(url_for('login'))
        return render_template('loginTemplate.html', status = "")
    else:
        f = 'storymaker.db'
        db = sqlite3.connect(f)
        c = db.cursor()
        q = "select user, sid from posts where sid == " + str(storyid)
        sel = c.execute(q)
        if session['user'] in sel:
            #redirect(url_for('viewstory'))
            return render_template('viewStory.html', text = 'nothing here yet...')
        else:
            return render_template('contributeForm.html')
