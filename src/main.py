#!/bin/env python3

## Python 2.7.X -> 3.0.X
## Main class: this class it is the orchestrator of the package.
### Author: Isham J. Araia @ None

import os
import yaml
import ast
import base
import time
from vault import Vault
from consul import Consul
from secretslib import Secrets

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

        self.secrets = Secrets(
            self.CONFIG['secrets']['aes'],
            self.CONFIG['secrets']['iv']
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
                shamir = ast.literal_eval(self._getSecret("shamir_keys"))
                self.vault.unseal(shamir)
            else:
                print(self.log('Instance status: UNSEALED.', 1))


    def _getSecret(self, data=str):
        """
        Get decrypted secrets from the backend.
        """
        path = "vau_secrets/{}".format(data)
        es = self.consul._get(path)
        return self.secrets.decrypt(es)


    def _saveSecrets(self, data=dict):
        """
        Save encrypted secrets to the backend.
        """
        for item in data:
            #Encrypt data and return a base64 conversion
            enc = self.secrets.encrypt(data[item])
            #Path where to push the data
            path = "vau_secrets/{}".format(item)
            print(self.log('Saving the secrets inside /{}'.format(path), 1))
            #Push action
            self.consul._put(path, enc)


    def main(self):
        """
        Check if the cluster is \
            initialized and start the control_loop.
        """
        if (self.vault.getInitStatus() != True and
                self.CONFIG['vault']['init'] == True):

            #Initialize the cluster
            print(self.log('Vault Cluster needs to be initialized.', 1))
            keys, rtk = self.vault.init(self.CONFIG['vault']['init-payload'])
            
            #Starting the control loop
            print(self.log('Storing the root token and the shamir keys ...', 1))
            self._saveSecrets({'shamir_keys': keys, 'root_token': rtk})

            print(self.log('Cluster initialized. Starting the control_loop...', 1))
            self.control_loop()

        if (self.vault.getInitStatus() != True and
                self.CONFIG['vault']['init'] == False):

                print(self.log('Another instance is initializing the cluster.', 1))
                time.sleep(self.CONFIG['join_timeout'])
                if self.vault.getInitStatus() != True:
                    raise Exception(self.log('Error during the cluster init.', 4))
                else:
                    print(self.log('Another instance has initialize the cluster. Starting the control_loop.', 1))
                    self.control_loop()

        #Starting the infinite control loop
        print(self.log('Vault Cluster already initialized.', 1))

        ## Try to get the old credentials if already stored \
        ## in the backend or save them there if not.
        try:
            self.consul._get('shamir_keys')
            self.consul._get('root_token')

        except ValueError:

            msg = 'Encrypt and save the secrets. '
            msg += 'Then you MUST delete them from the config.yml.'
            print(self.log(msg, 2))

            keys = self.CONFIG['shamir_keys']
            rtk = self.CONFIG['root_token']
            self._saveSecrets({'shamir_keys': keys, 'root_token': rtk})
        except:
            err = 'Error retriving the init keys&rtk'
            raise Exception(self.log(err, 4))

        print(self.log('Starting the control_loop ...', 1))
        self.control_loop()


if __name__ == '__main__':
    vau = Main()
    vau.main()
else:
    raise Exception('Non importable module')