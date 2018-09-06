##
## Python 2.7.X -> 3.0.X
### Minimal Backend API library
### Author: Isham J. Araia @ None
### Date: 20 - 08 - 2018

import requests as rq
import json
import sys
import base64
import common


class Backend():
    """
    This class is intended to handle 
        the backend connections and transactions.
    """

    def __init__(self, host='http://localhost:8500', path='/', token='token'):
        """
        Constructor method
        """

        ##Load common methods class
        self.base = common.Common()

        if not self.base._valid_url(host):
            self.base.log('Not a valid URL', 4)
            sys.exit(1)

        self.host = host
        self.token = token
        self.path = path
        

    def _std_headers(self):
        """
        Standard http headers for consul
        """
        return {
            'User-Agent': 'Vault Auto-Unsealing/0.0.1',
            'Content-Type': 'application/json',
            'X-Consul-Token': self.token
        }

    def _put(self, item, data):
        """
        Method to put info from the consul backend.
        """

        # Compose url to call
        url = "{}/{}/{}".format(
            self.host, 
            self.path,
            item
        )

        resp = rq.put(url, headers=self._std_headers(), data=str(data))

        return resp.content
    
    def _get(self, item):
        """
        Method to get info from the consul backend.
        """

        # Compose url to call
        url = "{}/{}/{}".format(
            self.host, 
            self.path,
            item
        )

        resp = rq.get(url, headers=self._std_headers())
        data = json.loads(resp.content)
        value = base64.b64decode(data[0]['Value'])

        return value

    
    def _delete(self, item):
        """
        Method to delete from the consul backend.
        """

        # Compose url to call
        url = "{}/{}/{}".format(
            self.host, 
            self.path,
            item
        )

        resp = rq.delete(url, headers=self._std_headers())

        return resp.content


def tests():
    """
    Simple testing method.
    To bring up the testing environment \
    use the docker container on ..backend/
    """

    test = Backend('http://test:8500', 'v1/kv/backend.py.testing', 'very-secret-token')
    print('Testing the _put() method:')
    print(test._put('object', {'key':'value'}))
    print('[X] SUCCESS\n---------\n')

    print('Testing the _get() method:')
    print(test._get('object'))
    print('[X] SUCCESS\n---------\n')

    print('Testing the _delete() method:')
    print(test._delete('object'))
    print('[X] SUCCESS\n---------\n')

    print('Backend testing finished with success.')

if __name__ == '__main__':
    tests()