import numpy

with open("../data/input.txt", 'r') as input_file:
    lines = input_file.readlines()

seven_segment_numbers = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]

def format_input(input_list):
    temp_output = []
    temp_input = []
    for input in input_list:
        temp_list = [input.rstrip("\n").split("|")]
        for index in temp_list:
            temp_input.append(index[0].split())
            temp_output.append(index[1].split())
    return temp_input, temp_output


def count_occurrences(outputs_list, number):
    count = 0
    for output in outputs_list:
        temp = [x for x in output if len(x) == len(number)]
        count += len(temp)
    return count


def get_wiring(input_list):
    seven_segment_display = {"a": "", "b": "", "c": "", "d": "", "e": "", "f": "", "g": ""}
    # 1. Get one
    one = [x for x in input_list if len(x) == len(seven_segment_numbers[1])][0]
    # 2. Get eight
    eight = [x for x in input_list if len(x) == len(seven_segment_numbers[8])][0]
    # 3. Get seven and wire to a
    seven = [x for x in input_list if len(x) == len(seven_segment_numbers[7])][0]
    a = compare_numbers(seven, one)
    seven_segment_display.update({"a": a})
    # 4. Get four
    four = [x for x in input_list if len(x) == len(seven_segment_numbers[4])][0]
    bd = compare_numbers(four, one)
    # 5. Get zero and wire to b and d
    possible_zeros = [x for x in input_list if len(x) == len(seven_segment_numbers[0])]
    zero = [x for x in possible_zeros if (list(bd)[0] in x and not list(bd)[1] in x) or (not list(bd)[0] in x and list(bd)[1] in x)][0]
    seven_segment_display.update({"b": [x for x in zero if (list(bd)[0] == x) or (list(bd)[1] == x)][0]})
    seven_segment_display.update({"d": compare_numbers(bd, seven_segment_display.get("b"))})
    # 6. Get five and wire to f, c, e and g
    possible_fives = [x for x in input_list if len(x) == len(seven_segment_numbers[5])]
    five = [x for x in possible_fives if (seven_segment_display.get("b") in x)][0]
    seven_segment_display.update({"f": [x for x in five if (list(one)[0] == x) or (list(one)[1] == x)][0]})
    seven_segment_display.update({"c": compare_numbers(one, seven_segment_display.get("f"))})
    seven_segment_display.update({"g": [x for x in five if not(x in seven_segment_display.values())][0]})
    seven_segment_display.update({"e": [x for x in eight if not(x in seven_segment_display.values())][0]})
    return seven_segment_display


def compare_numbers(number1, number2):
    for letter in number2:
        number1 = number1.replace(letter, "")
    return number1


def translate_numbers(display, temp_output):
    number = ""
    for output in temp_output:
        segments = ""
        for letter in output:
            segments += [actual_segment for actual_segment, wire in display.items() if letter == wire][0]
        segments = ''.join(str(item)for item in sorted(segments))
        number += str([index for index, x in enumerate(seven_segment_numbers) if segments == x][0])
    return number


def get_result(inputs_list, output_list):
    output_sum = 0
    for i, input in enumerate(inputs_list):
        wiring = get_wiring(input)
        output_sum += int(translate_numbers(wiring, output_list[i]))
    return output_sum


# --->Part1
inputs, outputs = format_input(lines)
amount_one = count_occurrences(outputs, seven_segment_numbers[1])
amount_four = count_occurrences(outputs, seven_segment_numbers[4])
amount_seven = count_occurrences(outputs, seven_segment_numbers[7])
amount_eight = count_occurrences(outputs, seven_segment_numbers[8])
print("Amount of 1, 4, 7 and 8: {}".format(amount_one + amount_four + amount_seven + amount_eight))

# --->Part2
inputs, outputs = format_input(lines)
result = get_result(inputs, outputs)
print("Result: {}".format(result))
