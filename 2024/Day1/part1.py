left_lst = []
right_lst = []

with open('data/input.txt', 'r') as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) >= 2: #Ensure at least 2 columns
            left_lst.append(int(parts[0]))
            right_lst.append(int(parts[1]))

def part1(left, right):
    sorted_left = sorted(left)
    sorted_right = sorted(right)

    differences = [abs(a - b) for a, b in zip(sorted_left, sorted_right)]
    return sum(differences)

def part2(left, right):
    similarity = [a * right.count(a) for a in left]
    return sum(similarity)
    

print(part1(left_lst, right_lst))
print(part2(left_lst, right_lst))