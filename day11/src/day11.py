with open("../data/input.txt") as input_file:
     squids = {(x, y): int(squid) for x, l in enumerate(input_file) for y, squid in enumerate(l.strip())}


def get_neighbors(x, y):
    return filter(squids.get, [(x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y + 1), (x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1)])


def iterations(rounds):
    count = 0
    for step in range(0, rounds):
        for squid in squids:
            squids[squid] += 1
        count += flashing()
        if sum(squids.values()) == 0:
            return step + 99
    return count


def flashing():
    count = 0
    flashing = {squid for squid in squids if squids[squid] > 9}
    while flashing:
        f = flashing.pop()
        squids[f] = 0
        count += 1
        for n in get_neighbors(*f):
            squids[n] += 1
            if squids[n] > 9:
                flashing.add(n)
    return count

# --->Part1
print("Result 1: {}".format(iterations(100)))

# --->Part2
print("Result 2: {}".format(iterations(1000)))


