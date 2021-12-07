import numpy

with open("../data/input.txt", 'r') as input_file:
    line = input_file.readlines()


def format_input():
    for position in line:
        temp_line = list(map(int, position.split(',')))
    return temp_line


def create_median(array):
    return int(numpy.median(array))


def count_used_fuel(start_positions, end_position, part2=False):
    movements = numpy.zeros(0, dtype=int)
    calculated_fuel = numpy.zeros(0, dtype=int)
    for start_position in start_positions:
        if start_position > end_position:
            movements = numpy.append(movements, (start_position - end_position))
        else:
            movements = numpy.append(movements, (end_position - start_position))
    if part2:
        for movement in movements:
            calculated_fuel = numpy.append(calculated_fuel, gaussian_formula(movement))
        return numpy.sum(calculated_fuel)
    total_fuel = numpy.sum(movements)
    return total_fuel


def gaussian_formula(position):
    return int((position**2+position)/2)


# --->Part1
horizontal_positions = numpy.array(format_input())
median = create_median(horizontal_positions)
fuel = count_used_fuel(horizontal_positions, median)
print("Fuel needed for part 1: {}".format(fuel))

# --->Part2
fuels = numpy.zeros(0, dtype=int)
horizontal_positions = numpy.array(format_input())
for x in range(max(horizontal_positions)):
    fuels = numpy.append(fuels, count_used_fuel(horizontal_positions, x, True))
print("Fuel needed for part 2: {}".format(min(fuels)))