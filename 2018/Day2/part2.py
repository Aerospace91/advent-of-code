from collections import Counter

with open('data/input.txt', 'r') as f:
    lines = f.read().splitlines()

twos = 0
threes = 0

for line in lines:
    c = Counter(line)
    if 2 in c.values():
        twos += 1
    if 3 in c.values():
        threes += 1

result = twos * threes
print(result)