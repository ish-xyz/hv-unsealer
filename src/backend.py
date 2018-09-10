##
## Python 2.7.X -> 3.0.X
### Minimal Backend API library
### Author: Isham J. Araia @ None
### Date: 20 - 08 - 2018

import sys
import common


class Backend(common.Common):
    """
    This class is intended to handle 
        the backend connections and transactions.
    """

    def __init__(self, host='http://localhost:8500', path='/', token='token'):
        """
        Constructor method
        """

        if not self._valid_url(host):
            self.log('Not a valid URL', 4)
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
        return super(Backend, self)._put(self._std_headers(), item, data)
    

    def _get(self, item):
        """
        Method to get info from the consul backend.
        """
        return super(Backend, self)._get(self._std_headers(), item)

    
    def _delete(self, item):
        """
        Method to delete from the consul backend.
        """
        return super(Backend, self)._delete(self._std_headers(), item)


if __name__ == '__main__':
    print("Import only.")
    pass