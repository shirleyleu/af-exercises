from .coordinate import Coordinate
import unittest


class Test(unittest.TestCase):
    def test_coordinate_eq(self):
        self.assertTrue(Coordinate(1, 2) == Coordinate(1, 2))
        self.assertFalse(Coordinate(2, 1) == Coordinate(1, 2))
        self.assertFalse(Coordinate(1, 3) == Coordinate(1, 2))
        self.assertFalse(Coordinate(2, 2) == Coordinate(1, 2))


if __name__ == '__main__':
    unittest.main()
