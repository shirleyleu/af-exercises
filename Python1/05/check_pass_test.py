from .check_pass import check_pass
import unittest


class Test(unittest.TestCase):
    def test_check_pass(self):
        self.assertFalse(check_pass("waytoolongpassword"))
        self.assertFalse(check_pass("short"))
        self.assertFalse(check_pass("lowercase1$"))
        self.assertFalse(check_pass("UPPER0#"))
        self.assertFalse(check_pass("noSpec1a7"))
        self.assertFalse(check_pass("noNuMb#r"))
        self.assertTrue(check_pass("P#$$w0rdOK"))


if __name__ == '__main__':
    unittest.main()
