import unittest
from main_source import hello_world

class MyTestCase(unittest.TestCase):
    def test_hello_message(self):
        self.assertEqual("Hello, sky", hello_world.hello_message())


if __name__ == '__main__':
    unittest.main()
