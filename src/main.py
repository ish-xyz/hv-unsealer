#!/bin/env python3

## Python 2.7.X -> 3.0.X
## Main class: this class it is the orchestrator of the package.
### Author: Isham J. Araia @ None

import os
import yaml
import base
import time
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
        while True:
            try:
                time.sleep(self.CONFIG['timeout'])
            except TypeError:
                err = 'You must use an INT as "timeout:" param in the config.yml'
                raise Exception(self.log(err, 3))

            if self.vault.getSealStatus() == True:
                print(self.log('Instance is sealed, proceed with the unsealing.', 2))
            else:
                print(self.log('Instance status: UNSEALED.', 1))


    def main(self):
        """
        Check if the cluster is initialized and start the control_loop.
        """

        if (self.vault.getInitStatus() != True and
                self.CONFIG['vault']['init'] == True):

            #Initialize the cluster
            print(self.log('Vault Cluster needs to be initialized.', 1)) 
            keys, rtk = self.vault.init(self.CONFIG['vault']['init-payload'])
            
            #Starting the control loop
            print(self.log('Storing the root token and the shamir keys ...', 1))
            ## Store the keys
            print(self.log('Cluster initialized. Starting the control_loop...', 1))

            self.control_loop()

        else:
            #Starting the control loop
            print(self.log('Vault Cluster already initialized.', 1))
            print(self.log('Starting the infinite loop ...', 1))
            self.control_loop()


if __name__ == '__main__':
    vau = Main()
    vau.main()
else:
    raise Exception('Non importable module')