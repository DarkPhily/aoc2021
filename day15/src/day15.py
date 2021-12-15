import numpy as np
import timeit

start_time = timeit.default_timer()
with open("../data/input.txt", "r") as input_file:
    array2d = [[int(digit) for digit in list(line.rstrip("\n"))] for line in input_file]
    chitons = np.array(array2d)
    chitons_dict = {coordinates: int(chiton) for coordinates, chiton in np.ndenumerate(chitons)}


def get_neighbours(x, y):
    return filter(chitons_dict.get, [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)])


def find_path(graph, start, end):
    distances = {coordinates: float("inf") for coordinates, _ in np.ndenumerate(graph)}
    visited = {coordinates: False for coordinates, _ in np.ndenumerate(graph)}
    distances[start] = 0
    while True:
        shortest_distance = float("inf")
        shortest_coordinate = -1
        for key, value in np.ndenumerate(graph):
            if distances[key] < shortest_distance and not visited[key]:
                shortest_distance = distances[key]
                shortest_coordinate = key
        # print("Visiting node {} with current distance {}".format(shortest_coordinate, shortest_distance))
        if shortest_coordinate == -1:
            return distances[(end[0]-1, end[1]-1)]
        for neighbour in get_neighbours(*shortest_coordinate):
            if graph[neighbour] != 0 and distances[neighbour] > distances[shortest_coordinate] + graph[neighbour]:
                distances[neighbour] = distances[shortest_coordinate] + graph[neighbour]
                # print("Updating distance of node {} to {}".format(neighbour, distances[neighbour]))
        visited[shortest_coordinate] = True


# --->Part1
print("Result 1: {}".format(find_path(chitons, (0, 0), chitons.shape)))






