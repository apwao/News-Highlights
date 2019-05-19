from flask import render_template
from app import app

@app.route('/')
def index():
    """
    A function than returns the home page when called upon
    """

    return render_template('index.html')