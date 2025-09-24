# ----------Author-----------
# Name: Ali Rizvi
# Date: 06-08-2025
# Email: 2410057@uad.ac.uk
# ---------------------------

# Import necessary libraries
from typing import List, Tuple
from point import Point
import matplotlib.pyplot as plt

# ------------ 6. Rendering with a PNG ... ------------


def render_mst(points: List[Point], 
               mst_edges: List[Tuple[Point, Point, float]],
               file_name: str) -> None:
    
    # Scaling factor to whance spacing in the plot.
    x_scale, y_scale = 7, 7

    # Creating plot, and setting its background color
    fig, ax = plt.subplots(figsize=(8, 8))
    fig.patch.set_facecolor("lightyellow")

    # Plot each edge in the MST as a red line between two points
    for u, v, weight in mst_edges:
        x_values = [u.get_x() * x_scale, v.get_x() * x_scale]
        y_values = [u.get_y() * y_scale, v.get_y() * y_scale]
        ax.plot(x_values, y_values, color='red', linewidth=2)
    
    # Prepare scaled coordinates for all points
    x_coords, y_coords = list(), list()
    
    # Collect all scaled x and y coords.
    for point in points:
        scaled_x = point.get_x() * x_scale
        x_coords.append(scaled_x)
    
    for point in points:
        scaled_y = point.get_y() * y_scale
        y_coords.append(scaled_y)

    # A few aesthetics
    ax.scatter(x_coords, y_coords, color='blue', s=50, zorder=5)

    ax.axis('off')
    plt.title("Minimum Spanning Tree (MST)", fontsize=14)
    plt.savefig(file_name, bbox_inches='tight', facecolor=fig.get_facecolor())
    print(f"Plot saved as '{file_name}'")