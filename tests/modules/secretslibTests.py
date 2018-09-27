##
## Python 2.7.X -> 3.0.X
### Consul Backend testing suite
### Author: Isham J. Araia @ None
### Date: 20 - 08 - 2018

import pathLoader
import unittest
import secretslib
import general

class TestSecretslib(unittest.TestCase):

    def setUp(self):
        """
        Setup the environment to test methods
        """
        config = general.General('tests-config.yml').CONFIG['secretslibTests']
        self.sc = secretslib.Secrets(config['aes'], config['iv'])

    def test_encrypt(self):
        """
        Test: secretlib.Secrets.encrypt()
        """
        mykey = 'test-encryption'
        self.assertNotEqual(self.sc.encrypt(mykey), mykey)

    def test_decrypt(self):
        """
        Test: secretlib.Secrets.decrypt()
        """
        mykey = 'test-encryption'
        ekey = self.sc.encrypt(mykey)
        self.assertEqual(self.sc.decrypt(ekey), mykey)


if __name__ == '__main__':
    unittest.main()
