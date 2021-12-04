with open("../data/input.txt", 'r') as input_file:
    lines = input_file.readlines()

drawn_numbers = lines.pop(0).rstrip("\n").split(',')
lists = []
boards = {}
board_counter = 1
for line in lines:
    value = line.rstrip("\n")
    if value != '':
        lists.append(value.split())
    if len(lists) == 5:
        for row in range(len(lists)):
            try:
                boards["board{}".format(board_counter)].append(lists.pop(0))
            except KeyError:
                board_row = [[]]
                board_row[0] = lists.pop(0)
                boards["board{}".format(board_counter)] = board_row
        board_counter += 1

#--->Part1
def check_number(element):
    for board in boards:
        for row in boards[board]:
            for i, number in enumerate(row):
                if number == element:
                    row[i] = 'X'

def check_for_winners():
    winners = []
    for board in boards:
        count_row = [0, 0, 0, 0, 0]
        count_column = [0, 0, 0, 0, 0]
        for j, row in enumerate(boards[board]):
            for i, number in enumerate(row):
                if number == 'X':
                    count_row[j] += 1
                    count_column[i] += 1
        if 5 in count_row or 5 in count_column:
            winners.insert(0, board)
    return winners

for element in drawn_numbers:
    check_number(element)
    winners = check_for_winners()
    if len(winners) != 0:
        sum = 0
        for winner in winners:
            for row in boards[winner]:
                for char in row:
                    if char != 'X':
                        sum += int(char)
        print("Result: {}".format(sum*int(element)))
        break

#--->Part2
for element in drawn_numbers:
    check_number(element)
    winners = check_for_winners()
    if len(winners) != 0:
        print(len(boards))
        if len(boards) != 1:
            for winner in winners:
                boards.pop(winner)
        else:
            sum = 0
            for winner in winners:
                for row in boards[winner]:
                    for char in row:
                        if char != 'X':
                            sum += int(char)
            print("Result: {}".format(sum * int(element)))



