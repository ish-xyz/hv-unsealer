##
## Python 2.7.X -> 3.0.X
### Consul Backend testing suite
### Author: Isham J. Araia @ None
### Date: 20 - 08 - 2018

import modulesLoader
import unittest
import consul
import baseTests

class TestConsul(unittest.TestCase):

    def setUp(self):
        """
        Setup the environment to test methods
        """
        self.init_payload = { 
            "secret_shares": 10,
            "secret_threshold": 5
        }
    
    def test_vault_init(self):
        pass

    def tearDown(self):
        """
        Teardown function.
        """
        pass

if __name__ == '__main__':
    unittest.main()
