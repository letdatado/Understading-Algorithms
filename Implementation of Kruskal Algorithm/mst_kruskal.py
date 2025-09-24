# ----------Author-----------
# Name: Ali Rizvi
# Date: 06-08-2025
# Email: 2410057@uad.ac.uk
# ---------------------------

# Import necessary libraries
from typing import List, Tuple
from point import Point
from graph import Graph

# ------------ 5. Kruskal Minimum Spanning Trees ... ------------


class KruskalMST:
    def __init__(self, graph: Graph):
        self.graph = graph
        
        # Each vertex initially belongs to its own set 
        self.parent_index: List[int] = list(range(len(graph.vertices)))
        
        # This will store the final MST edges: (Point, Point, distance)
        self.minimum_spanning_tree: List[Tuple[Point, Point, float]] = []

    def find_root(self, 
                  vertex_index: int) -> int:
        # Recursively finds the root of the set and applies path compression
        if self.parent_index[vertex_index] != vertex_index:
             # Update parent to root
            self.parent_index[vertex_index] = self.find_root(self.parent_index[
                vertex_index])
        return self.parent_index[vertex_index]
    
    def connect_points(self, index_u: int, index_v: int) -> bool:
        # Combines two disjoint sets if they are not already connected
        root_u = self.find_root(index_u)
        root_v = self.find_root(index_v)

        # Attempt to connect both vertices by checking if the belong 
        # ... to different sets to avoid creating cycles.
        if root_u != root_v:
            self.parent_index[root_v] = root_u
            return True
        else:
            return False

    @staticmethod
    def get_weight(edge: Tuple[int, int, float]) -> float:
        weight_index = 2  # Just to capture the distance from edge data.
        return edge[weight_index]
    
    def run(self) -> List[Tuple[Point, Point, float]]:
        # Sort the edges by weight (distance)
        sorted_edges = sorted(self.graph.edges, key=self.get_weight)
        
        # Go through each edge and try to add it to the MST
        for vertex_u_index, vertex_v_index, edge_weight in sorted_edges:
            if self.connect_points(vertex_u_index, vertex_v_index):
                point_u = self.graph.vertices[vertex_u_index]
                point_v = self.graph.vertices[vertex_v_index]
                self.minimum_spanning_tree.append((point_u, 
                                                   point_v, 
                                                   edge_weight))

            # Stop early if we already have (V - 1) edges
            if len(self.minimum_spanning_tree) == len(self.graph.vertices) - 1:
                break

        return self.minimum_spanning_tree
