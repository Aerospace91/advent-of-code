lines = list(map(int, open('input.txt').read().splitlines()))

increased = 0
start = lines[0]
for num in lines:
    if num > start:
        increased += 1
    start = num

print(increased)