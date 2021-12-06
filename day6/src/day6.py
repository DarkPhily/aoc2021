import numpy

with open("../data/input.txt", 'r') as input_file:
    line = input_file.readlines()


def format_input():
    for fish in line:
        temp_lines = list(map(int, fish.split(',')))
    return temp_lines


def pass_day(array):
    return numpy.roll(array, -1)


def spawn_and_reset_fish(array):
    if array[0] > 0:
        array[7] += array[0]
    return array


def days_to_pass(array, days):
    for day in range(days):
        array = spawn_and_reset_fish(array)
        array = pass_day(array)
    return array


def count_days(array):
    temp_array = numpy.zeros(9, dtype=numpy.longlong)
    unique, counts = numpy.unique(array, return_counts=True)
    counts_dict = dict(zip(unique, counts))
    for key in counts_dict:
        temp_array[key] = counts_dict[key]
    return temp_array


def count_fish(array):
    counted_fish = 0
    for i in array:
        counted_fish += i
    return counted_fish

# --->Part1
population = numpy.array(format_input())
population = count_days(population)
population = days_to_pass(population, 80)
countPopulation = count_fish(population)
print("Result1: {}".format(countPopulation))

# --->Part2
population = numpy.array(format_input())
population = count_days(population)
population = days_to_pass(population, 256)
countPopulation = count_fish(population)
print("Result2: {}".format(countPopulation))
