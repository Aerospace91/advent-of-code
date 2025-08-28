with open('data/input.txt', 'r') as f:
    lines = f.read().splitlines()

list_of_twos = 0
list_of_threes = 0
for line in lines:
    temp_dict = {}
    for char in line:
        if char not in temp_dict:
            temp_dict[char] = 1
        else:
            temp_dict[char] += 1
        
    for key, value in temp_dict.items():
        if value == 2:
            list_of_twos += 1
            break
        if value == 3:
            list_of_threes += 1
            break
        
result = list_of_twos * list_of_threes
print(result)