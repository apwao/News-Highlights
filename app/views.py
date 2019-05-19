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
    A function that returns the top headlines of different news sources when the user clicks 
    on a news source
    """
    # get the news sources
    news_sources = get_sources()
    
    #Get topheadlines for the specified source
    top_headlines = get_topheadlines(source)
    
    return render_template('topheadlines.html', news_sources = new_sources, topheadlines = topheadlines)



