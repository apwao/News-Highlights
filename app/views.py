from flask import render_template, request,redirect,url_for
from app import app
from .request import get_sources, get_top_headlines, get_everything

@app.route('/')
def index():
    """
    A function than returns the home page when called upon
    """
    #get all available news sources
    news_sources = get_sources()
    
    #get all news articles available
    everything = get_everything()
    print(everything)
    # title = 'Home - Find all the current news at your convinience'

    return render_template('index.html', news_sources = news_sources, everything = everything)


@app.route('/source/<source>')
def topheadlines(source):
    """
    A function that returns the top headlines of different news sources when the user clicks 
    on a news source
    """
    # get the news sources
    news_sources = get_sources()
    
    #Get topheadlines for the specified source
    top_headlines = get_top_headlines(source)
    
    
    
    return render_template('topheadlines.html', news_sources = news_sources, topheadlines = top_headlines)




