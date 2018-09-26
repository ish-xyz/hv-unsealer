#!/bin/env python3

##
## Main class

import os
import yaml
import base
from vault import Vault
from consul import Consul

class Main(base.Base):
    """
    Main class to orchestrate the package logic.
    """

    def __init__(self):
        """
        Constructor method
        """
        self.CONFIG = self._configLoad()

        self.vault = Vault(
                self.CONFIG['vault']['address'],
                self.CONFIG['vault']['path']
                )

        self.consul = Consul(
            self.CONFIG['consul']['address'],
            self.CONFIG['consul']['path'],
            self.CONFIG['consul']['acl-token'],
        )

    def _configLoad(self):
        """
        Configuration load class
        """
        try:
            with open(os.environ['VAU_CONFIG'], 'r') as stream:
                try:
                    return yaml.load(stream)
                except yaml.YAMLError as exc:
                    raise Exception(self.log(exc, 4))
        except KeyError:
            err = 'Use VAU_CONFIG to indicate the configuration file.'
            raise Exception(self.log(err, 4))

    def control_loop(self):
        """
        An infinite routine that will check \
            the vault status and perform operations such as unseal and init.
        """
        pass

    def main(self):
        """
        Check if the cluster is initialized and start the control_loop.
        """

        if (self.vault.getInitStatus() == True and
                self.CONFIG['vault']['init'] == True):

            print(self.log('Vault Cluster needs to be initialized.', 1)) 
            keys, rtk = self.vault.init()
            print(self.log('Retriving the root token and the shamir keys ...'))
            print(keys, rtk)
        else:
            print(self.log('Vault Cluster already initialized.', 1))
            print(self.log('Starting the infinite loop ...', 1))


if __name__ == '__main__':
    vau = Main()
    vau.main()
else:
    raise Exception('Non importable module')