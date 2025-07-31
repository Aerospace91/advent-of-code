import re

with open("data/input.txt", "r") as f:
    data = f.read()
    
def part1(data):
    def extract_muls(s):
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.findall(pattern, s)
        return matches
    return sum(int(x) * int(y) for x, y in extract_muls(data))

def part2(data):
    pattern = r"don't\(\)|do\(\)|mul\((\d{1,3}),(\d{1,3})\)"
    enabled = True
    total = 0
    
    for match in re.finditer(pattern, data):
        if match.group(0) == "do()":
            enabled = True
        elif match.group(0) == "don't()":
            enabled = False
        elif match.group(0).startswith("mul("):
            if enabled:
                x = int(match.group(1))
                y = int (match.group(2))
                total += x * y
    
    return total


print(part1(data))
print(part2(data))