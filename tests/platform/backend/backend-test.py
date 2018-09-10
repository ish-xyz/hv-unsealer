import loader
import unittest
import backend

class BackendGet(unittest.TestCase):

    def setUp(self):
        self.be_test = backend.Backend('http://cube:8500', 'v1/kv/backend.py.testing', 'very-secret-token')
        self.be_test._put('get-test', {'key':'value'})

    def test_backend_get(self):
        self.assertEqual(self.be_test._get('get-test'), "{'key': 'value'}")
    
    def tearDown(self):
        self.be_test._delete('get-test')


class TestBackendPut(unittest.TestCase):

    def setUp(self):
        self.be_test = backend.Backend('http://cube:8500', 'v1/kv/backend.py.testing', 'very-secret-token')

    def test_backend_put(self):
        self.assertEqual(self.be_test._put('put-test', {'testing':'true'}), 'true')
    
    def tearDown(self):
        self.be_test._delete('put-test')


class TestBackendDel(unittest.TestCase):

    def setUp(self):
        self.be_test = backend.Backend('http://cube:8500', 'v1/kv/backend.py.testing', 'very-secret-token')
        self.be_test._put('del-test', {'testing':'true'})

    def test_backend_put(self):
        self.assertEqual(self.be_test._delete('del-test'), 'true')



if __name__ == '__main__':
    unittest.main()