import numpy

with open("../data/input.txt", 'r') as input_file:
    line = input_file.readlines()

# --->Part1
def format_input():#ok
    for fish in line:
        temp_lines = list(map(int, fish.split(',')))
    return temp_lines


def pass_day(array):
    for index, fish in numpy.ndenumerate(array):
        array[index] = fish - 1
    return array


def spawn_fish(array):
    count = count_0(array)
    appending_array = numpy.full(count, 9)
    array = numpy.append(array, appending_array)
    return array


def reset_fish_day(array):
    return numpy.where(array == 0, 7, array)


def days_to_pass(array, days):
    for day in range(days):
        array = spawn_fish(array)
        array = reset_fish_day(array)
        array = pass_day(array)
    return array


def count_fish(array):
    return array.size


def count_0(array):
    unique, counts = numpy.unique(array, return_counts=True)
    counts_dict = dict(zip(unique, counts))
    if 0 in counts_dict:
        counted_0 = counts_dict.pop(0)
    else:
        counted_0 = 0
    return counted_0




population = numpy.array(format_input())
population = days_to_pass(population, 80)
countPopulation = count_fish(population)
print("Result1: {}".format(countPopulation))

# --->Part2
population = numpy.array(format_input())
population = days_to_pass(population, 256)
countPopulation = count_fish(population)
print("Result2: {}".format(countPopulation))
