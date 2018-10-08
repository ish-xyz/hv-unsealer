##
## Python 2.7.X -> 3.0.X
### Consul Backend testing suite
### Author: Isham J. Araia @ None
### Date: 20 - 08 - 2018

import pathLoader
import unittest
import main
import consul
import common
import time

class TestVault(unittest.TestCase):

    def setUp(self):
        """
        Unit tests setup method
        """
        self.config =  common.Common('tests-config.yml').CONFIG['main_test']

	#Setup the consul connection. Consul will be used as D.backend.

        self.consul = consul.Consul(
			self.config['consul-addres'],
			self.config['consul-path'],
			self.config['consul-token']
		)
	self.vault = vault.Vault(
			self.config['vault-address'],
			self.config['vault-path']
		)

	# Test ->  save, get, control_loop, configLoad


    def tearDown(self):
        """
        Teardown function.
        """
        #De-initialize the Vault cluster
        #wait for the cluster setup
        self.consul._delete('vault/?recurse=true')


if __name__ == '__main__':
    unittest.main()
