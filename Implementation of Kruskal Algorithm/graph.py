# ----------Author-----------
# Name: Ali Rizvi
# Date: 06-08-2025
# Email: 2410057@uad.ac.uk
# ---------------------------

# Import necessary libraries
from typing import List, Tuple
from point import Point

# ------------ 4. Implementing a Graph Class ... ------------


class Graph:
    def __init__(self, 
                 vertices: List[Point], 
                 edges: List[Tuple[int, int, float]]):
        # List of all points in the graph AKA Nodes
        self.vertices = vertices
        
        # List of edges, where each edge is a tuple (index1, index2, weight)
        # ... index1, index2 are the positions of the vertices
        # ... weight is the distance between two points.
        self.edges = edges