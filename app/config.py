class Config:
    """
    The main configurations parent class with configurations common to both 
    development and production
    """
    ALL_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    TOP_HEADLINES_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    EVERYTHING_BASE_URL = 'https://newsapi.org/v2/everything?q=trending&apiKey={}'

class ProdConfig(Config):
    """
    Production configuration child class with configurations relevant 
    during production

    Args:
    Config: The parent configuration class with General configuration settings
    """
    pass

class DevConfig(Config):
    """
    Development configuration child class with configurations relevant during
    the development stage

    Args:Args:
    Config: The parent configuration class with General configuration settings
    """

    DEBUG = True