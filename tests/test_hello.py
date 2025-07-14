import unittest
from hello import say_hello

class HelloTest(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello("Pascal"), "Hello, Pascal!")

if __name__ == "__main__":
    unittest.main()
