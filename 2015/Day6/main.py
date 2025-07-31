with open('input.txt') as f: lines = [line.strip() for line in f]

major_list = [[0] * 1000 for i in range(1000)]

for line in lines:
    command = line.split(' ')
    if command[0] == 'turn' and command[1] == 'on':
        start_x, start_y = map(int, command[2].split(','))
        end_x, end_y = map(int, command[4].split(','))
        for i in range(start_x, end_x):
            for j in range(start_y - 1, len(major_list[i])):
                major_list[i][j] = 1
                
    elif command[0] == 'turn' and command[1] == 'off':
        start_x, start_y = map(int, command[2].split(','))
        end_x, end_y = map(int, command[4].split(','))
        for i in range(start_x, end_x):
            for j in range(start_y, len(major_list[i])):
                major_list[i][j] = 0
                
    elif command[0] == 'toggle':
        start_x, start_y = map(int, command[1].split(','))
        end_x, end_y = map(int, command[3].split(','))
        for i in range(start_x, end_x):
            for j in range(start_y, len(major_list[i])):
                if major_list[i][j] == 0:
                    major_list[i][j] = 1
                if major_list[i][j] == 1:
                    major_list[i][j] = 0
                
sum_of_list = 0    
for line in major_list:
    sum_of_list += sum(line)
    
print(sum_of_list)