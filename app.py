from flask import Flask, render_template
from utils import newStory
app = Flask(__name__)

@app.route("/makepost/")
def make():
    return render_template("make_post.html")

@app.route("/results/", methods = ["POST"])
def result():
    return "hi"
if __name__ == '__main__':
    app.debug = True
    app.run()
