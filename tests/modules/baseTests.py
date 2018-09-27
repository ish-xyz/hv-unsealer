##
## Python 2.7.X -> 3.0.X
### Consul Backend testing suite
### Author: Isham J. Araia @ None
### Date: 20 - 08 - 2018

import pathLoader
import unittest
import base
import general

class TestBase(unittest.TestCase):

    def setUp(self):
        """
        Setup the environment to test methods
        """
        #Load the general configuration
        #self.config = general.General('tests-config.yml').CONFIG['baseTests']
        self.base = base.Base()


    def test_valid_url(self):
        """
        Test: base.Base._valid_url()
        """
        self.assertEqual(self.base._valid_url('http://0.0.0.0/'), True)
        self.assertEqual(self.base._valid_url('not-an-url'), False)
        

    def test_log(self):
        """
        Test: base.Base.log()
        """
        self.assertEqual(type(self.base.log('Testing the log function', 1)), str)
        

if __name__ == '__main__':
    unittest.main()
