from flask import Flask, render_template, request, session, url_for
import sqlite3
app = Flask(__name__)

@app.route('/contribute/<int:storyid>')
def contribute(storyid):    
    if 'user' not in session:
        #redirect(url_for('login'))
    else:
        f = 'storymaker.db'
        db = sqlite3.connect(f)
        c = db.cursor()        
        q = "select user, sid from posts where sid == " + storyid
        sel = c.execute(q)
        if session['user'] in sel:
            #redirect(url_for('viewstory'))
        else:
            return render_template('contributeForm.html')
        
        
        
