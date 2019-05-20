import unittest
from app.models import Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources(12,'Washington Post','A News Source you can trust','https://www.bbc.com/news/entertainment-arts-48117944','fashion','English','Britain')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))