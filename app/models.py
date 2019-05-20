class Sources:
    """
    Class sources that acts as a blueprint for creating a sample
    source to be displayed on the homepage
    """

    def __init__(self, id, name, description, url, category, language, country):
        """
        __init__ method that initializes the parameters required to
        create an instance of class Sources
        """
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
        

class TopHeadlines:
    """
    Class TopHeadlines that acts as a blueprint for creating instances of
    headlines from a given source
    """

    def __init__(self, author, title, description, url, urlToImage, publishedAt):
        """
        __init__ method to initialize parameters required to create 
        instances of class TopHeadlines
        """
        
        self.author = author
        self.title = title
        self.description = description
        self.url = url 
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        
    
class Everything:
    """
    Class Everything that acts as a blueprint for creating 
    instances of unfiltered news
    """

    def __init__(self, author, title, description, url, urlToImage, publishedAt):
        """
        __init__ method to initialize attributes of the class Everything
        """
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt