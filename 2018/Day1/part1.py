with open('data/input.txt', 'r') as f:
    lines = f.read().splitlines()
    
numbers = [int(s) for s in lines]

print(sum(numbers))