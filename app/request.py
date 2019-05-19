from app import app
import urllib.request, json
from .models import sources, everything, topheadlines,

#Accessing the classes within the files
Sources = sources.Sources
Everything = everything.Everything
TopHeadlines = topheadlines.TopHeadlines

#Accessing the API key
api_key = app.config['NEWS_API_KEY']


#Accessing the sources base url
sources_base_url =app.config['ALL_SOURCES_BASE_URL']
topheadlines_base_url = app.config['TOP_HEADLINES_BASE_URL']
everything_base_url = app.config['EVERYTHING_BASE_URL']

def get_sources():
    """
    get_sources function to make the api request for all the news
    sources available in the news website
    """
    #Combine base url with api key to get final url
    get_sources_url = sources_base_url.format(api_key)
    
    #send request and obtain response from server
    with urllib.request.urlopen(get_sources_url) as url:
        #obtain the content of the response and store in variable
        get_sources_data = url.read()
        #use json to model the data into objects
        get_sources_response = json.loads(get_sources_data)
        
        #create variable to store the final results
        sources_results = None
        
        #Confirm that the sources key within the response is not empty
        if get_sources_response['sources']:
            #if not empty, assign to new variable
            source_results_list = get_sources_response['sources']
            #process results further using the Sources class 
            source_results = process_source_results(source_results_list)
     #return processed results       
    return source_results
            
            
            
            
        
        
    
    
    