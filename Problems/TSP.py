import itertools
import numpy as np
from geopy.distance import geodesic

def calculate_total_distance(route, distance_matrix):
    return distance_matrix[route[:-1], route[1:]].sum()

def find_optimal_route(house_locations):
    house_names = list(house_locations.keys())
    num_houses = len(house_names)
    
    coordinates = np.array(list(house_locations.values()))
    distance_matrix = np.zeros((num_houses, num_houses))
    
    for i in range(num_houses):
        for j in range(i + 1, num_houses):
            distance_matrix[i, j] = distance_matrix[j, i] = geodesic(
                coordinates[i], coordinates[j]
            ).kilometers
    
    all_permutations = list(itertools.permutations(range(num_houses)))
    
    optimal_route = None
    min_distance = float('inf')
    
    for permutation in all_permutations:
        route = np.array(permutation)
        distance = calculate_total_distance(route, distance_matrix)
        
        if distance < min_distance:
            min_distance = distance
            optimal_route = route
    
    return [house_names[idx] for idx in optimal_route]

house_locations = {
    "House A": (40.7128, -74.0060),
    "House B": (34.0522, -118.2437),
    "House C": (41.8781, -87.6298),
    "House D": (37.7749, -122.4194)
}

optimal_route = find_optimal_route(house_locations)
print("Optimal Route:", optimal_route)
