lines = []
with open("../data/input.txt", 'r') as input_file:
    lines = input_file.readlines()

count = 0
for x in range(0, len(lines)-3):
    sum1 = int(lines[x]) + int(lines[x+1]) + int(lines[x+2])
    sum2 = int(lines[x+1]) + int(lines[x+2]) + int(lines[x+3])
    if sum1 < sum2:
        count += 1

print(count)
