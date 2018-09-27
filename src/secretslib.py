#!/bin/env python3

## Python 2.7.X -> 3.0.X
### Secret class: Encryption and Decryption class - AES
### Author: Isham J. Araia @ None

from Crypto.Cipher import AES
import os
import base

class Secret(base.Base):
    """
    This class is intended to handle 
        the in transit keys decryption and encryption.
    """

    def __init__(self, aes, iv):
        """
        Constructor method: __init__
        """
        self.aes = aes
        self.iv = iv
        
    def encrypt(self, message):
        """
        In-transit encryption method
        """
        AES.new(self.aes, AES.MODE_CFB, self.iv)
        try:
            instance = AES.new(self.aes, AES.MODE_CFB, self.iv)
            return instance.encrypt(message)
        except:
            err = 'Error during the in transit encryption.'
            raise Exception(self.log(err, 3))


    def decrypt(self, message):
        """
        In-transit decryption method
        """
        try:
            instance = AES.new(self.aes, AES.MODE_CFB, self.iv)
            return instance.decrypt(message)
        except:
            err = 'Error during the in transit decryption.'
            raise Exception(self.log(err), 3)


if __name__ == '__main__':
    print("Import only.")