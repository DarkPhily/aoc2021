import numpy as np
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder

with open("../data/input.txt", "r") as input_file:
    array2d = [[int(digit) for digit in list(line.rstrip("\n"))] for line in input_file]
    chitons = np.array(array2d)


def find_path(graph, start, end):
    finder = DijkstraFinder()
    start = grid.node(*start)
    end = grid.node(end[0]-1, end[1]-1)
    path, runs = finder.find_path(start, end, graph)
    return path


def get_full_map(graph):
    map_0 = graph
    map_1 = graph + 1
    map_1 = np.where(map_1 == 10, 1, map_1)
    map_2 = map_1 + 1
    map_2 = np.where(map_2 == 10, 1, map_2)
    map_3 = map_2 + 1
    map_3 = np.where(map_3 == 10, 1, map_3)
    map_4 = map_3 + 1
    map_4 = np.where(map_4 == 10, 1, map_4)
    map_5 = map_4 + 1
    map_5 = np.where(map_5 == 10, 1, map_5)
    map_6 = map_5 + 1
    map_6 = np.where(map_6 == 10, 1, map_6)
    map_7 = map_6 + 1
    map_7 = np.where(map_7 == 10, 1, map_7)
    map_8 = map_7 + 1
    map_8 = np.where(map_8 == 10, 1, map_8)
    row_1 = np.concatenate((map_0, map_1, map_2, map_3, map_4), axis=1)
    row_2 = np.concatenate((map_1, map_2, map_3, map_4, map_5), axis=1)
    row_3 = np.concatenate((map_2, map_3, map_4, map_5, map_6), axis=1)
    row_4 = np.concatenate((map_3, map_4, map_5, map_6, map_7), axis=1)
    row_5 = np.concatenate((map_4, map_5, map_6, map_7, map_8), axis=1)
    return np.concatenate((row_1, row_2, row_3, row_4, row_5), axis=0)


def count_weight(path, map, start):
    return sum(map[tuple(reversed(point))] for point in path) - map[tuple(reversed(start))]


# --->Part1
grid = Grid(matrix=chitons)
optimal_path = find_path(grid, (0, 0), chitons.shape)
print("Result 1: {}".format(count_weight(optimal_path, chitons, (0, 0))))


# --->Part2
full_map = get_full_map(chitons)
grid = Grid(matrix=full_map)
optimal_path = find_path(grid, (0, 0), full_map.shape)
print("Result 2: {}".format(count_weight(optimal_path, full_map, (0, 0))))




