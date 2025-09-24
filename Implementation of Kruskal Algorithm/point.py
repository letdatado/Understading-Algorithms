# ----------Author-----------
# Name: Ali Rizvi
# Date: 06-08-2025
# Email: 2410057@uad.ac.uk
# ---------------------------

# Import necessary libraries
from typing import List, Tuple
from data_loader import Y_VALUES

# ------------ 2. Implementing a Point class ... ------------


class Point:
    def __init__(self, x: int, y: int):
        # Initialize points x and y 
        self.x = x
        self.y = y

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_distance(self, target: "Point") -> float:
        # Compute the distance using Euclidean Formula
        diff_x = target.get_x() - self.x
        diff_y = target.get_y() - self.y
        return (diff_x ** 2 + diff_y ** 2) ** 0.5

    def __str__(self) -> str:
        # Representation as a string of Point
        return f"Point({self.x},{self.y})"


# ---------- 3. Finding all neighbours within a certain distance ... ----------

def generate_list_of_points() -> List[Point]:
    list_of_all_points: List[Point] = []
    for index, value in enumerate(Y_VALUES):
        x_value = index + 1 # Couple x value with the corresponding y
        y_value = value
        list_of_all_points.append(Point(x_value, y_value)) # Compile the list
    return list_of_all_points 


def find_neighbours(list_of_all_points: List[Point], 
                    max_distance: float) -> List[Tuple[int, int, float]]:
    list_of_edges: List[Tuple[int, int, float]] = []
    # Loop over all the unique points 
    for index, origin_point in enumerate(list_of_all_points):
        for second_index in range(index + 1, len(list_of_all_points)):
            target_point = list_of_all_points[second_index]
            # Obtain the distance between the points
            distance = origin_point.get_distance(target_point)
            if 0 < distance <= max_distance:
                # Append if distance is acceptable
                list_of_edges.append((index, second_index, distance))

    return list_of_edges
