lines = open('input.txt').read().splitlines()
pos, depth, aim = 0, 0, 0
directions = []
for line in lines:
    split = line.split()
    directions.append([split[0], split[1]])

for direction in directions:
    if direction[0] == 'forward':
        pos += int(direction[1])
        depth += aim * int(direction[1])
    elif direction[0] == 'down':
        aim += int(direction[1])
    elif direction[0] == 'up':
        aim -= int(direction[1])

print(pos, depth, aim)
print(pos * depth)