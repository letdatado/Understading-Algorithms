# ----------Author-----------
# Name: Ali Rizvi
# Date: 06-08-2025
# Email: 2410057@uad.ac.uk
# ---------------------------
import unittest
from pathlib import Path
from point import Point
from render import render_mst


class TestRender(unittest.TestCase):
    def test_render(self):
        # Create two simple points
        p1 = Point(1, 1)
        p2 = Point(2, 2)
        # Define a MST edge between them
        mst_edges = [(p1, p2, 1.0)]
        
        # Please don't confuse this with the final MST
        file_path = Path("unittesting_delete_it.png")
        
        # Call the render function to create the plot image
        render_mst([p1, p2], mst_edges, file_name=str(file_path))
        self.assertTrue(file_path.exists())