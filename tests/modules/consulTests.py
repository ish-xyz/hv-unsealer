##
## Python 2.7.X -> 3.0.X
### Consul Backend testing suite
### Author: Isham J. Araia @ None
### Date: 20 - 08 - 2018

import pathLoader
import unittest
import consul
import general

class TestConsul(unittest.TestCase):

    def setUp(self):
        """
        Setup the environment to test methods
        """
        config = general.General('tests-config.yml').CONFIG['consulTests']
        self.get_test = consul.Consul(config['address'], config['path'], config['acl-token'])
        self.put_test = consul.Consul(config['address'], config['path'], config['acl-token'])
        self.del_test = consul.Consul(config['address'], config['path'], config['acl-token'])

        #Push items
        self.del_test._put('del', {'del':'true'})
        self.get_test._put('get', {'get':'true'})

    def test_consul_get(self):
        """
        Test: consul.Consul._get()
        """
        self.assertEqual(self.get_test._get('get'), '{"get": "true"}')

    def test_consul_put(self):
        """
        Test: consul.Consul._put()
        """
        self.assertEqual(self.put_test._put('put', {'put':'true'}), 'true')
    
    def test_consul_del(self):
        """
        Test: consul.Consul._del()
        """
        self.assertEqual(self.del_test._delete('del'), 'true')
    
    def tearDown(self):
        """
        Teardown function.
        """
        self.get_test._delete('get')
        self.put_test._delete('put')
        self.put_test._delete('del')


if __name__ == '__main__':
    unittest.main()
