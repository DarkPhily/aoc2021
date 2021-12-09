from math import prod

with open("../data/input.txt", "r") as input_file:
    input_array = input_file.readlines()


def format_input(array):
    temp_gird = []
    for line in array:
        temp_gird.append(list(line.rstrip("\n")))
    return temp_gird


def get_neighbors(x, y):
    up = grid[y-1][x]
    left = grid[y][x-1]
    if y == 0:
        up = "null"
    if y + 1 == len(grid):
        down = "null"
    else:
        down = grid[y + 1][x]
    if x == 0:
        left = "null"
    if x + 1 == len(grid[0]):
        right = "null"
    else:
        right = grid[y][x + 1]
    return [(y-1, x), (y+1, x), (y, x-1), (y, x+1)], [up, down, left, right]


def is_low(array):
    low_points = []
    low_points_coordinates = []
    for y, row in enumerate(array):
        for x, point in enumerate(row):
            is_true = []
            coordinates, neighbors = get_neighbors(x, y)
            for n in neighbors:
                if n == "null":
                    is_true.append(True)
                elif point < n:
                    is_true.append(True)
                else:
                    is_true.append(False)
            if all(is_true):
                low_points.append(point)
                low_points_coordinates.append((y, x))
    return low_points, low_points_coordinates


def count_basins(coordinate):
    #basins.append(1 + grid[coordinate[0]][coordinate[1]])
    if grid[coordinate[0]][coordinate[1]] == 9:
        return 0
    del grid[coordinate[0]][coordinate[1]]
    coordinates, neighbors = get_neighbors(coordinate[1], coordinate[0])
    for i, coordinate in enumerate(coordinates):
        if neighbors[i] == "null":
            continue
        else:
            return 1 + sum(map(count_basins, neighbors(coordinate[1], coordinate[0])))
    #return 1 + sum(basins)


# --->Part1
grid = format_input(input_array)
low_points, low_points_coordinates = is_low(grid)
print("Result 1: {}".format(sum(int(x) + 1 for x in low_points)))

# --->Part2
basins = []
for p in low_points_coordinates:
    basins.append(count_basins(p))
basins = [count_basins(p) for p in low_points_coordinates]


