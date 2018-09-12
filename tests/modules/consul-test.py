##
## Python 2.7.X -> 3.0.X
### Consul Backend testing suite
### Author: Isham J. Araia @ None
### Date: 20 - 08 - 2018

import loader
import tests_common
import unittest
import consul

class TestConsulGet(unittest.TestCase):

    def setUp(self):
        self.be_test = consul.Consul('http://consulmod:8500', 'v1/kv/consul.py.testing', 'very-secret-token')
        self.be_test._put('get-test', {'key':'value'})

    def test_consul_get(self):
        self.assertEqual(self.be_test._get('get-test'), "{'key': 'value'}")
    
    def tearDown(self):
        self.be_test._delete('get-test')


class TestConsulPut(unittest.TestCase):

    def setUp(self):
        self.be_test = consul.Consul('http://consulmod:8500', 'v1/kv/consul.py.testing', 'very-secret-token')

    def test_consul_put(self):
        self.assertEqual(self.be_test._put('put-test', {'testing':'true'}), 'true')
    
    def tearDown(self):
        self.be_test._delete('put-test')


class TestConsulDel(unittest.TestCase):

    def setUp(self):
        self.be_test = consul.Consul('http://consulmod:8500', 'v1/kv/consul.py.testing', 'very-secret-token')
        self.be_test._put('del-test', {'testing':'true'})

    def test_consul_put(self):
        self.assertEqual(self.be_test._delete('del-test'), 'true')



if __name__ == '__main__':
    unittest.main()
