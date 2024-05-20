lines = list(map(int, open('input.txt').read().splitlines()))

increased = 0
window_sum = []

for i in range(0, len(lines)):
    if i == len(lines) - 2:
        break
    window_sum.append(lines[i] + lines[i + 1] + lines[i + 2])

start = window_sum[0]

for num in window_sum:
    if num > start:
        increased += 1
    start = num

print(increased)