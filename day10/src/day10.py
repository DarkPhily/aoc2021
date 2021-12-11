with open("../data/input.txt", "r") as input_file:
    input_array = input_file.readlines()

opening_brackets = ["(", "[", "{", "<"]

def check_input(array):
    stack = []
    for bracket in array:
        if bracket in opening_brackets:
            stack.append(bracket)
        else:
            if not stack:
                return bracket
            current_bracket = stack.pop()
            if current_bracket == "(":
                if bracket != ")":
                    return bracket
            if current_bracket == "[":
                if bracket != "]":
                    return bracket
            if current_bracket == "{":
                if bracket != "}":
                    return bracket
            if current_bracket == "<":
                if bracket != ">":
                    return bracket
    if stack:
        return stack


def complete_incomplete(array):
    stack = []
    for bracket in reversed(array):
        if bracket == "(":
            stack.append(")")
        if bracket == "[":
            stack.append("]")
        if bracket == "{":
            stack.append("}")
        if bracket == "<":
            stack.append(">")
    return stack


def is_corrupted(array):
    return [x for x in array if len(x) == 1]


def is_incomplete(array):
    return [x for x in array if len(x) > 1]


def get_points(array):
    point_dict = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = 0
    for bracket in array:
        score += point_dict.get(bracket)
    return score


def get_score(array):
    point_dict = {")": 1, "]": 2, "}": 3, ">": 4}
    score = 0
    for bracket in array:
        score = score*5 + point_dict.get(bracket)
    return score


def get_middle(array):
    middle = float(len(array))/2
    return array[int(middle - .5)]


# --->Part1
checked_input = [check_input(x.rstrip("\n")) for x in input_array]
corrupted = is_corrupted(checked_input)
print("Score: {}".format(get_points(corrupted)))

# --->Part2
incomplete = is_incomplete(checked_input)
complete = [complete_incomplete(x) for x in incomplete]
scores = [get_score(x) for x in complete]
middle = get_middle(sorted(scores))
print("Score: {}".format(get_middle(sorted(scores))))

