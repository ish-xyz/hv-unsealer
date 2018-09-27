#!/bin/env python3

## Python 2.7.X -> 3.0.X
### Vault class: Minimal Hashicorp Vault API library.
### Author: Isham J. Araia @ None

import requests as rq
import json
import base64
import base

class Vault(base.Base):
    """ Module used to retrive the 
        token and init&unseal the vault endpoint.
    """
    def __init__(self, host, path=''):
        """
        Class constructor
        Inputs:
            endpoint -> vault endpoint to unseal
        """
        if not self._valid_url(host):
            raise Exception(self.log('Not a valid URL', 4))

        self.host = host
        self.path = path

    def _std_headers(self):
        """
        Standard http headers for vault
        """
        return {
            'User-Agent': 'Vault Auto-Unsealing/0.0.1',
            'Content-Type': 'application/json'
        }

    def _get(self):
        pass

    def _put(self):
        pass

    def _post(self): 
        pass

    def _delete(self):
        pass

    def init(self, payload):
        """
        Method used to initialize the Hashicorp vault cluster.
        The function will just initialize the cluster and only if it is needed.
        Return: (keys -> array), (root_token -> string)
        """
        #Check if the cluster it's already initialized
        #init and parse
        if self.getInitStatus() != True:
            resp = super(Vault, self)._put(self._std_headers(), 'sys/init', payload)
            data = json.loads(resp)

            return data['keys'], data['root_token']
        else:
            print(self.log('The Vault cluter it has been already initialized.', 1))
            return True, True


    def getInitStatus(self):
        """
        Get the Vault cluster
         initialization status
        """
        resp = super(Vault, self)._get(self._std_headers(), 'sys/init')
        return json.loads(resp)['initialized']

    def getSealStatus(self):
        """
        Get the cluster status (seal or unseal)
        """
        resp = super(Vault, self)._get(self._std_headers(), 'sys/seal-status')
        return json.loads(resp)['sealed']

    def unseal(self, keys=[]) :
        """
        Method used only to unsueal the vault server.
        """
        for key in keys:
            data = { "key": key }
            resp = super(Vault, self)._put(self._std_headers(), 'sys/unseal', data)
        
        result = json.loads(resp)

        try:
            return result['sealed']
        except:
            raise Exception(
                        self.log(
                            "Error during the unseal. Details: {}".format(resp),
                            4
                        ))
