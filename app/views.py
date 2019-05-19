from flask import render_template
from app import app

@app.route('/')
def index():
    """
    A function than returns the home page when called upon
    """

    title = 'Home - Find all the current news at your convinience'

    return render_template('index.html' title = title)



