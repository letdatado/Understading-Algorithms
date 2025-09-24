# ----------Author-----------
# Name: Ali Rizvi
# Date: 06-08-2025
# Email: 2410057@uad.ac.uk
# ---------------------------

# Import necessary libraries 

from data_loader import verify_y_values, Y_VALUES, GIVEN_HASH, GIVEN_STRING
from point import generate_list_of_points, find_neighbours
from graph import Graph
from mst_kruskal import KruskalMST
from render import render_mst

if __name__ == "__main__":
    
    verify_y_values(GIVEN_STRING, GIVEN_HASH, Y_VALUES)
    points = generate_list_of_points()
    edges = find_neighbours(points, max_distance=20)
    graph = Graph(points, edges)
    mst_k = KruskalMST(graph).run()
    render_mst(points, mst_k, "kruskal_mst_output_ali_rizvi_2410057.png")