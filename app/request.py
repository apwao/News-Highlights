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

def process_source_results(news_sources_list):
    """
    process_source_results function to model the source_results from API
    into an instance of class Sources
    """
    #return type of process_sources_results made to a list
    source_results = []
    
    for source_item in news_sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')
        
        #create an instance of class Sources
        source_object = Sources(id,name,description,url,category,language,country)
        source_results.append(source_object)
        
    return source_results

def get_topheadlines(source):
    """
    get_topheadlines method that takes in the name of a specific source
    and returns the top-headlines of that source
    """
    #final combined url
    get_top_headlines_url = topheadlines_base_url.format(source, api_key)
    
    with urllib.request.urlopen("get_top_headlines_url") as url:
        topheadlines_data = url.read()
        topheadlines_response = json.loads(topheadlines_data)
        
        topheadlines_results = None
        
        if topheadlines_response['articles']:
            topheadlines_results_list = topheadlines_response['articles']
            topheadlines_results = process_topheadlines_results(topheadlines_results_list)
    
    return topheadlines_results    
            
def process_topheadlines_results(topheadlines_results_list):
    """
    process topheadlines_results function to model the response into 
    an instance of class TopHeadlines 
    """
    
    topheadlines_results[]
    
    for topheadlines_item in topheadlines_results_list:
        author = topheadlines_item.get('author')
        title = topheadlines_item.get('title')
        description = topheadlines_item.get('description')
        url = topheadlines_item.get('url')
        urlToImage = topheadlines_item.get('urlToImage')
        publishedAt = topheadlines_item.get('publishedAt')
        
        
        topheadlines_object = TopHeadlines(author,title,description,url, urlToImage, publishedAt)
        topheadlines_results.append(topheadlines_object)
        
    return topheadlines_results

 
def get_everything():
    """
    function get_everything that returns all the news available 
    within the news website
    """
    
    get_everything_url = everything_base_url.format(api_key)
    
    with urllib.request.urlopen(get_everything_url) as url:
        get_everything_data = url.read()
        get_everything_response = json.loads(get_everything_data)
       
        everything_results = None
        
        if get_everything_response['articles']:
            everything_results_list = get_everything_response['articles']
            everything_results = process_everything_results(everything_results_list)
   
    return everything_results

def process_everything_results(everything_results_list):
    """
    function process_everything_results that models all the news results
    into an instance of class Everything
    """
    everything_results = []
    
    for everything_item in everything_results_list:
        author = everything_item.get('author')
        title = everything_item.get('title')
        description = everything_item.get('description')
        url = everything_item.get('url')
        urlToImage = everything_item.get('urlToImage')
        publishedAt = everything_item.get('publishedAt')
        
        everything_object = Everything(author, title, description, url, urlToImage, publishedAt)
        everything_results.append(everything_object)
        
    return everything_results

            
              
        



    
            
            
            
            
        
        
    
    
    