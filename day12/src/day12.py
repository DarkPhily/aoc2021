with open("../data/input.txt", "r") as input_file:
    file = input_file.readlines()


def format_input():
    caves = {}
    for line in file:
        key, value = line.rstrip("\n").split("-")
        caves[key] = []
        caves[value] = []
    for line in file:
        key, value = line.rstrip("\n").split("-")
        caves[key] += [value]
        caves[value] += [key]
    return caves


def find_paths(visited=[], cave="start"):
    if cave == "end":
        return 1
    if cave in visited:
        if cave == "start":
            return 0
        if cave.islower():
            return 0
    return sum(find_paths(visited+[cave], cave=c) for c in cave_system[cave])


def find_paths_2(visited=[], cave="start", small_cave_visited=False):
    if cave == "end":
        return 1
    if cave in visited:
        if cave == "start":
            return 0
        if cave.islower():
            if small_cave_visited:
                return 0
            else:
                small_cave_visited = True
    return sum(find_paths_2(visited + [cave], cave=c, small_cave_visited=small_cave_visited) for c in cave_system[cave])


# --->Part1
cave_system = format_input()
print("Result 1: {}".format(find_paths()))

# --->Part2
print("Result 2: {}".format(find_paths_2()))
