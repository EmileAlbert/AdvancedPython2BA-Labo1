# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        #Test échoue
        self.assertEqual(utils.fact(3),5)
        #Test échoue
        with self.assertRaises(ValueError):
            utils.fact(1)
    
    def test_roots(self):
        #Test échoue
        self.assertEqual(utils.roots(1,1,0),(4,1))
    
    '''def test_integrate(self):
        # À compléter...
        pass'''

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())