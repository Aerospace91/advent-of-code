line = open('input.txt').read()

test_case = '()())'

sum = 0
count = 0
is_basement = False
basement_step = None
for char in line:
    count += 1
    if char == '(':
        sum += 1
    elif char == ')':
        sum -= 1
        if is_basement == False and sum < 0:
            is_basement = True
            basement_step = count

print(sum)
print(basement_step)