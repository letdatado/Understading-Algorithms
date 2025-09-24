# ----------Author-----------
# Name: Ali Rizvi
# Date: 06-08-2025
# Email: 2410057@uad.ac.uk
# ---------------------------

import unittest
from point import Point
from graph import Graph
from mst_kruskal import KruskalMST


class TestKruskal(unittest.TestCase):
    def test_kruskal(self):
        
        # Define three points forming a triangle
        # ... with 3 edges with weights
        points = [Point(0, 0), Point(0, 1), Point(1, 1)]
        edges = [(0, 1, 1), (1, 2, 1), (0, 2, 2)]
        
        # Create Graph and compute MST using Kruskal's algo
        g = Graph(points, edges)
        mst = KruskalMST(g).run()
        
        # Test assertion that MST contain exactly 2 edges for 3 points
        self.assertEqual(len(mst), 2)
        # Test assertion that MST's weight should be 2.
        self.assertEqual(sum(weight for i1, i2, weight in mst), 2)