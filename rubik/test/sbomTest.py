import unittest
import app

class SbomTest(unittest.TestCase):


    def test_sbom_100_ShouldReturnAuthorName(self):
        myName = 'hzs0093'
        result = app._getAuthor('../../')
        resultingAuthorName = result['author']
        self.assertEqual(resultingAuthorName, myName)

