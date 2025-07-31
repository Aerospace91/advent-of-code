with open('data/input.txt', 'r') as f:
    data = f.read().splitlines()
    
report = [[int(x) for x in s.split()] for s in data]

def part1(report):
    
    def is_valid(line):
        diffs = [b - a for a, b in zip(line, line[1:])]
        increasing = all(d > 0 for d in diffs)
        decreasing = all(d < 0 for d in diffs)
        valid_steps = all(abs(d) in (1, 2, 3) for d in diffs)
        return (increasing or decreasing) and valid_steps
    
    return [is_valid(line) for line in report]

def part2(report):
    
    def is_safe(line):
        diffs = [b - a for a, b in zip(line, line[1:])]
        increasing = all(d > 0 for d in diffs)
        decreasing = all(d < 0 for d in diffs)
        valid_steps = all(abs(d) in (1, 2, 3) for d in diffs)
        return (increasing or decreasing) and valid_steps
    
    safe_count = 0
    for line in report:
        if is_safe(line):
            safe_count += 1
        else:
            found = False
            for i in range(len(line)):
                new_line = line[:i] + line[i + 1:]
                if is_safe(new_line):
                    safe_count += 1
                    found = True
                    break
                
    return safe_count
    

print(part1(report).count(True))
print(part2(report))