user_input = open('input.txt').read()
# user_input = '2x3x4'

total_wrapping = 0
total_ribbon = 0

lines = user_input.strip().split('\n')

for present in lines:
    length, width, height = map(int, present.split('x'))
    num_list = sorted([length, width, height])
    surface_area = (2 * length * width) + (2 * width * height) + (2 * height * length)
    slack = num_list[0] * num_list[1]
    total_wrapping += surface_area + slack
    ribbon = (2 * num_list[0]) + (2 * num_list[1])
    bow = height * width * length
    total_ribbon += ribbon + bow

print(total_wrapping)
print(total_ribbon)