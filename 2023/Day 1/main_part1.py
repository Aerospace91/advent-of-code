import re

lines = open('input.txt').read().splitlines()

sum = 0
for line in lines:
    num_list = []
    digit_list = []
    res = re.findall(r'\d+', line)
    for string in res:
        num_list.append(num)
    for num in num_list:
        for digit in num:
            digit_list.append(digit)
    sum += int(digit_list[0] + digit_list[-1])

print(sum)