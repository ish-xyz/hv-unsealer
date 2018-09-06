#!/bin/env python3

import requests
import json

class executor():
    """ Module used to retrive the 
        token and unsueal the vault endpoint.
        This class will also initialize the cluster if it's needed.
    """
    def __init__(self, endpoint, key, storage):
        """
        Class constructor
        Inputs:
            endpoint -> vault endpoint to unseal
            key -> encryption key AES
            storage -> distributed backend system

        """
        self.endpoint = endpoint
        self.key = key
        self.storage = storage

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
