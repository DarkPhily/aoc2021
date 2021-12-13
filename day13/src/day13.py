import numpy as np
from parse import findall

with open("../data/input.txt", "r") as input_file:
    lines = input_file.read().splitlines()


def draw_paper():
    max_x = 0
    max_y = 0
    for line in lines:
        if line != '':
            x, y = line.split(",")
            if int(x) > max_x:
                max_x = int(x)
            if int(y) > max_y:
                max_y = int(y)
        else:
            break
    temp_paper = np.zeros((max_y + 1, max_x + 1), bool)
    for line in lines:
        if line != '':
            x, y = line.split(",")
            temp_paper[int(y)][int(x)] = True
        else:
            return temp_paper


def fold(part, paper):
    for line in lines:
        for axis, i in findall('{:l}={:d}', line):
            if axis == 'y':
                new_paper = np.delete(paper, i, 0)
                upper, lower = np.array_split(new_paper, 2, axis=0)
                lower = np.flip(lower, 0)
                for index, value in np.ndenumerate(lower):
                    if value:
                        upper[index] = value
                paper = upper
            else:
                new_paper = np.delete(paper, i, 1)
                left, right = np.array_split(new_paper, 2, 1)
                right = np.flip(right, 1)
                for index, value in np.ndenumerate(right):
                    if value:
                        left[index] = value
                paper = left
            if part == 1:
                return np.count_nonzero(paper)
    return paper

# --->Part1
paper = draw_paper()
dots = fold(1, paper)
print("Result 1: {}".format(dots))

# --->Part2
paper = draw_paper()
letters = fold(2, paper)
print("Result 2:")
print(np.array2string(letters, separator='', formatter={'bool': {0: ' ', 1: '█'}.get}))
