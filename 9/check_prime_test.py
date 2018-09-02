from .check_prime import is_prime
import unittest


class Test(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(111))
        self.assertTrue(is_prime(109))


if __name__ == '__main__':
    unittest.main()
