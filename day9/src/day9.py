from math import prod

with open("../data/input.txt", "r") as input_file:
    input_array = input_file.readlines()


def format_input(array):
    temp_dict = {}
    for y, list in enumerate(array):
        for x, value in enumerate(list):
            if value == "\n":
                continue
            temp_dict[(x, y)] = value
    return temp_dict


def get_neighbors(x, y):
    temp_list = []
    if (x, y-1) in grid:
        up = (x, y-1)
        temp_list.append(up)
    if (x, y+1) in grid:
        down = (x, y+1)
        temp_list.append(down)
    if (x-1, y) in grid:
        left = (x-1, y)
        temp_list.append(left)
    if (x+1, y) in grid:
        right = (x+1, y)
        temp_list.append(right)
    return temp_list


def is_low(point):
    return all(grid[point] < grid[neighbor] for neighbor in get_neighbors(*point))


def get_low_points(map):
    points = []
    for m in map:
        if is_low(m):
            points.append(m)
    return points


def count_basins(point):
    if point in grid:
        if int(grid[point]) == 9:
            return 0
        del grid[point]
        return 1 + sum(map(count_basins, get_neighbors(*point)))
    else:
        return 0


# --->Part1
grid = format_input(input_array)
low_points = get_low_points(grid)
print("Result 1: {}".format(sum(int(grid[x]) + 1 for x in low_points)))

# --->Part2
basins = [count_basins(point) for point in low_points]
print("Result 2: {}".format(prod(sorted(basins)[-3:])))


