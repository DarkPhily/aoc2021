from collections import Counter

with open("../data/input.txt", "r") as input_file:
    start = input_file.readline().rstrip("\n")
    input_file.readline()
    rules = input_file.read().split("\n")

rules = dict(rule.split(" -> ") for rule in rules)


def get_counts():
    char = list(start)
    temp_pairs = Counter()
    temp_chars = Counter(char)
    for index, letter in enumerate(char):
        if index + 1 == len(char):
            return temp_pairs, temp_chars
        else:
            temp_pairs[letter + char[index + 1]] = 1


def iterations(rounds):
    for _ in range(rounds):
        for key, count in pairs.copy().items():
            first_letter, second_letter = list(key)
            new_letter = rules[key]
            pairs[key] -= count
            pairs[first_letter + new_letter] += count
            pairs[new_letter + second_letter] += count
            chars[new_letter] += count


def count():
    sorted_values = sorted(chars.values())
    return sorted_values[-1] - sorted_values[0]


# --->Part1
pairs, chars = get_counts()
iterations(10)
print("Result 1: {}".format(count()))

# --->Part2
pairs, chars = get_counts()
iterations(40)
print("Result 2: {}".format(count()))
