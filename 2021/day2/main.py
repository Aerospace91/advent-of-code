lines = open('input.txt').read().splitlines()
pos, depth = 0, 0
directions = []
for line in lines:
    split = line.split()
    directions.append([split[0], split[1]])

for direction in directions:
    if direction[0] == 'forward':
        pos += int(direction[1])
    elif direction[0] == 'down':
        depth += int(direction[1])
    elif direction[0] == 'up':
        depth -= int(direction[1])

print(pos, depth)
print(pos * depth)