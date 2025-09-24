# ----------Author-----------
# Name: Ali Rizvi
# Date: 06-08-2025
# Email: 2410057@uad.ac.uk
# ---------------------------

import unittest
from point import Point
from graph import Graph


class TestGraph(unittest.TestCase):
    def test_graph_structure(self):
        # Define two points and an edge with a weight
        points = [Point(0, 0), Point(1, 1)]
        edges = [(0, 1, 1.41)]
        
        # Create Graph
        g = Graph(points, edges)
        
        # Assert that the values are stored correctly
        self.assertEqual(g.vertices, points)
        self.assertEqual(g.edges, edges)
