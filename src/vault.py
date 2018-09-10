#!/bin/env python3

import requests as rq
import json
import sys
import base64
import common

class Vault(common.Common):
    """ Module used to retrive the 
        token and init&unseal the vault endpoint.
    """
    def __init__(self, endpoint, key, storage_type):
        """
        Class constructor
        Inputs:
            endpoint -> vault endpoint to unseal
            key -> encryption key AES
            storage -> distributed backend system

        """
        self.endpoint = endpoint
        self.key = key
    
    def _get(self):
        pass

    def _put(self):
        pass

    def _post(self):
        pass

    def _del(self):
        pass

    def init(self):
        """
        Method used to initialize the Hashicorp vault setup.
        The function will just initialize the cluster only if it is needed.
        """
        pass

    def unseal(self, unsueal_keys=[], minkey=3) :
        """
        Method used only to unsueal the vault server.
        """
        pass