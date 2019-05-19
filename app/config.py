class Config:
    """
    The main configurations parent class with configurations common to both 
    development and production
    """
    pass

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