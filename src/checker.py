#!/bin/env python3

import requests
import json
import backend

class Monitor():
    """
    This class it's used to monitor the vault \
    service across multiple instances.
    """

    def __init__(self, backend, key):
        """
        ^description^
        """