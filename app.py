from flask import Flask, render_template, request
from utils import newStory
app = Flask(__name__)

@app.route("/makepost/")
def make():
    return render_template("make_post.html")

@app.route("/results/", methods = ["POST"])
def result():
    r = request.form
    post = r['post']
    return newStory.submit(post)
    
if __name__ == '__main__':
    app.debug = True
    app.run()
