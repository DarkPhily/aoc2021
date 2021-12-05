import numpy

with open("../data/input.txt", 'r') as input_file:
    lines = input_file.readlines()


def format_input():
    temp_lines = []
    for line in lines:
        value = line.rstrip("\n")
        temp_lines.append(list(map(int, value.replace(' -> ', ',').split(','))))
    return temp_lines


def check_for_non_diagonal(temp_lines):
    temp_non_diagonal = []
    for straight_line in temp_lines:
        if (straight_line[0] == straight_line[2]) or (straight_line[1] == straight_line[3]):
            temp_non_diagonal.append(straight_line)
    return temp_non_diagonal


def generate_array(temp_lines):
    temp_max = max(max(temp_lines))
    return numpy.zeros((temp_max + 1, temp_max + 1))


def draw_lines(temp_lines, temp_matrix):
    for line in temp_lines:
        if line[0] == line[2]:
            if line[1] > line[3]:
                for i in range(line[3], line[1] + 1):
                    temp_matrix[i][line[0]] += 1
            else:
                for i in range(line[1], line[3] + 1):
                    temp_matrix[i][line[0]] += 1
        elif line[1] == line[3]:
            if line[0] > line[2]:
                for i in range(line[2], line[0] + 1):
                    temp_matrix[line[1]][i] += 1
            else:
                for i in range(line[0], line[2] + 1):
                    temp_matrix[line[1]][i] += 1
        elif line[0] > line[2] and line[1] > line[3]:
            for i, value in enumerate(range(line[2], line[0] + 1)):
                temp_matrix[line[3]+i][value] += 1
        elif line[2] > line[0] and line[3] > line[1]:
            for i, value in enumerate(range(line[0], line[2] + 1)):
                temp_matrix[line[1]+i][value] += 1
        elif line[0] > line[2] and line[3] > line[1]:
            for i, value in enumerate(range(line[2], line[0] + 1)):
                temp_matrix[line[3]-i][value] += 1
        elif line[2] > line[0] and line[1] > line[3]:
            for i, value in enumerate(range(line[0], line[2] + 1)):
                temp_matrix[line[1]-i][value] +=1

    return temp_matrix


def count_occurrences(temp_matrix):
    result = 0
    unique, counts = numpy.unique(temp_matrix, return_counts=True)
    counts_dict = dict(zip(unique, counts))
    counts_dict.pop(0)
    counts_dict.pop(1)
    for count in counts_dict.values():
        result += count
    return result


# --->Part1
straight_lines = format_input()
non_diagonal = check_for_non_diagonal(straight_lines)
matrix = generate_array(non_diagonal)
matrix = draw_lines(non_diagonal, matrix)
counts = count_occurrences(matrix)
print("Result 1: {}".format(counts))

# --->Part2
straight_lines = format_input()
matrix = generate_array(straight_lines)
matrix = draw_lines(straight_lines, matrix)
counts = count_occurrences(matrix)
print("Result 2: {}".format(counts))
