# ----------Author-----------
# Name: Ali Rizvi
# Date: 06-08-2025
# Email: 2410057@uad.ac.uk
# ---------------------------

import unittest
import math
from point import Point


class TestPoint(unittest.TestCase):
    def test_get_x_y(self):
        p = Point(2, 5)
        # X and Y coords should come out as 2 and 5, respectively.
        self.assertEqual(p.get_x(), 2)
        self.assertEqual(p.get_y(), 5)

    def test_get_distance_zero(self):
        # Should confirm that the distance b/w a point and itself
        # ... is Zero.
        p = Point(1, 1)
        self.assertEqual(p.get_distance(p), 0.0)

    def test_get_distance_known(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        # Test the distance calculation using a 3-4-5 triangle,
        # ... where the distance between p1 and p2 is exactly 5.
        self.assertTrue(math.isclose(p1.get_distance(p2), 5.0))
