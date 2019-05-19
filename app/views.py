from flask import render_template
from app import app

@app.route('/')
def index():
    """
    A function than returns the home page when called upon
    """
    #get all available news sources
    news_sources = get_sources()
    
    #get all news articles available
    everything = get_everything()

    title = 'Home - Find all the current news at your convinience'

    return render_template('index.html' title = title, new_sources = news_sources, everything = everything)

@app.route('/news/<source>')
def topheadlines(source):
    """
    A function that returns the 
    """



