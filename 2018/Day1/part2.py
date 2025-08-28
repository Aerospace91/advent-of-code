with open('data/input.txt', 'r') as f:
    lines = f.read().splitlines()
    
numbers = [int(s) for s in lines]

seen = set()
current_freg = 0
found = False

while not found:
    for number in numbers:
        current_freg += number
        if current_freg in seen:
            print(current_freg)
            found = True
            break
        seen.add(current_freg)
