import unittest
from app.models import TopHeadlines

class TopHeadlinesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_topheadline = TopHeadlines('Ivy','I Will Be My Own Stuntsman','An inspiring story on taking risks','https://www.bbc.com/news/entertainment-arts-48117944','https://www.bbc.com/news/entertainment','NewYorkTimes')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_topheadline,TopHeadlines))