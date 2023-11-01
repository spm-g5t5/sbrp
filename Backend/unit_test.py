import unittest
from app import *

class CISetupTest(unittest.TestCase):
    def test_hello(self):

        res = hello()
        self.assertEqual(res, "Welcome to SBRP")

if __name__ == "__main__":
    unittest.main()
