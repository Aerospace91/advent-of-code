user_input = open('input.txt').read()

total = 0

lines = user_input.strip().split('\n')

for present in lines:
    length, width, height = map(int, present.split('x'))
    num_list = sorted([length, width, height])
    surface_area = (2 * length * width) + (2 * width * height) + (2 * height * length)
    slack = num_list[0] * num_list[1]
    total += surface_area + slack

print(total)