import re
from collections import defaultdict

fabric = defaultdict(int)

with open('data/input.txt', 'r') as f:
    lines = f.read().splitlines()
    
for line in lines:
    #Parsing
    claim = re.match(r'#\d+ @ (\d+),(\d+): (\d+)x(\d+)', line)
    left, top, width, height = map(int, claim.groups())
    for x in range(left, left + width):
        for y in range(top, top + height):
            fabric[(x, y)] += 1
            
overlap_count = sum(1 for v in fabric.values() if v > 1)
print(overlap_count)