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
        

        