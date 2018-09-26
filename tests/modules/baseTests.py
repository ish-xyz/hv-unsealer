##
## Python 2.7.X -> 3.0.X
### Consul Backend testing suite
### Author: Isham J. Araia @ None
### Date: 20 - 08 - 2018

import pathLoader
import unittest
import vault
import consul
import general
import time

class TestVault(unittest.TestCase):

    def setUp(self):
        """
        Setup the environment to test methods
        """
        #Load the general configuration and setup the vault connection
        self.config = general.General('tests-config.yml').CONFIG['vaultTests']
        self.vault = vault.Vault(
                self.config['address'],
                self.config['path']
            )
        #Setup the Vault Backend Connection
        self.consul = consul.Consul(
                self.config['consul'],
                self.config['consul-path'],
                self.config['consul-token']
            )

    def test_vault_init(self):
        """
        Test: vault.Vault.init()
        """
        keys, root_token = self.vault.init(self.config['init-payload'])

        self.assertEqual(len(keys), self.config['init-payload']['secret_shares'])
        self.assertEqual(len(root_token), 36)
        self.consul._delete('vault/?recurse=true')
        

    def test_vault_unseal(self):
        """
        Test: vault.Vault.unseal()
        """
        keys, root_token = self.vault.init(self.config['init-payload'])
        self.assertEqual(self.vault.unseal(keys), False)
        self.consul._delete('vault/?recurse=true')

    def tearDown(self):
        """
        Teardown function.
        """
        #De-initialize the Vault cluster
        #wait for the cluster setup
        self.consul._delete('vault/?recurse=true')
        

if __name__ == '__main__':
    unittest.main()
