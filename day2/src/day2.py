lines = []
with open("../data/input.txt", 'r') as input_file:
    lines = input_file.readlines()

#--->Part1
forward = 0
down = 0
up = 0
for line in lines:
    list = line.split()
    if list[0] == 'forward':
        forward = forward + int(list[1])
    elif list[0] == 'down':
        down = down + int(list[1])
    elif list[0] == 'up':
        up = up + int(list[1])

print("depth position: {}\nhorizontal position: {}\nresult: {}".format(down-up, forward, (down-up)*forward))

#--->Part2

forward = 0
aim = 0
depth = 0
for line in lines:
    list = line.split()
    if list[0] == 'forward':
        forward += int(list[1])
        depth += (aim * int(list[1]))
    elif list[0] == 'down':
        aim += int(list[1])
    elif list[0] == 'up':
        aim -= int(list[1])

print("Depth: {}\nHorizontal position: {}\nResult: {}".format(depth, forward, depth*forward))
