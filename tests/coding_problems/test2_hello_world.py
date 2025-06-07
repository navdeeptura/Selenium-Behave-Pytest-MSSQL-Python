import unittest
from hello_world import abc

class HelloWorldTest(unittest.TestCase):
    def test_hello(self):
        msg = "Test if hello world is returned"
        self.assertEqual(abc(), "Hello World!", msg=msg)

if __name__ == '__main__':
    unittest.main()