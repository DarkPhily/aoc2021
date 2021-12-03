import regex as re

with open("../data/input.txt", 'r') as input_file:
    lines = input_file.readlines()

#--->Part 1
lists = []
for line in lines:
    value = line.rstrip("\n")
    lists.append(list(value))

gamma = ''
epsilon = ''
for x in range(len(lists[0])):
    column = ''
    for y in range(len(lists)):
        column += str(lists[y][x])
    zero = column.count('0')
    one = column.count('1')
    if zero > one:
        gamma += str('0')
        epsilon += str('1')
    else:
        gamma += str('1')
        epsilon += str('0')

print("Gamma in binary: {}\nGamma in decimal: {}\nEpsilon in binary: {}\nEpsilon in decimal: {}\nPower consumption: {}"
      .format(gamma, int(gamma, 2), epsilon, int(epsilon, 2), int(gamma, 2)*int(epsilon, 2)))

#--->Part2
lists = []
for line in lines:
    value = line.rstrip("\n")
    lists.append(list(value))

def return_count(list, digit):
    #for x in range(len(list[0])):
    column = ''
    for y in range(len(list)):
        column += str(list[y][digit])
    zero = column.count('0')
    one = column.count('1')
    return [zero, one]

def return_new_list(list, compare_value):
    for row in range(len(list)):
        if list[row][digit] == compare_value:
            indices.append(row)
    for index in indices:
        temporary_list.append(list[index])
    return temporary_list

O2 = lists
for digit in range(len(O2)):
    if len(O2) != 1:
        count = return_count(O2, digit)
        indices = []
        temporary_list = []
        if count[0] > count[1]:
            O2 = return_new_list(O2, '0')
        elif count[0] < count[1]:
            O2 = return_new_list(O2, '1')
        elif count[0] == count[1]:
            O2 = return_new_list(O2, '1')
    else:
        break
oxygen_generator_rating = ''.join(O2[0])
print("Oxygen generator rating: {}".format(oxygen_generator_rating))

CO2 = lists
for digit in range(len(CO2)):
    if len(CO2) != 1:
        count = return_count(CO2, digit)
        indices = []
        temporary_list = []
        if count[0] < count[1]:
            CO2 = return_new_list(CO2, '0')
        elif count[0] > count[1]:
            CO2 = return_new_list(CO2, '1')
        elif count[0] == count[1]:
            CO2 = return_new_list(CO2, '0')
    else:
        break
co2_scrubber_rating = ''.join(CO2[0])
print("CO2 scrubber rating: {}".format(co2_scrubber_rating))
print("Oxygen generator rating: {}\nCO2 scrubber rating: {}\nLife support rating: {}"
      .format(int(oxygen_generator_rating, 2), int(co2_scrubber_rating, 2), int(oxygen_generator_rating, 2)*int(co2_scrubber_rating, 2)))




