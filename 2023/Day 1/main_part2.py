lines = open('input.txt').read().splitlines()

word_nums = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
sum = 0

lines2 = {line: ({}, {}) for line in lines}

for word in word_nums:
    for line in lines2:
        if line.find(word) != -1:
            lines2[line][0][line.find(word)] = word
            lines2[line][1][line[::-1].find(word[::-1])] = word
    

nums2 = []
for line in lines2:
    index_0, index_1 = lines2[line]
    first = word_nums[index_0[min(index_0)]]
    last = word_nums[index_1[min(index_1)]]
    nums2.append(int(first + last))
    
for num in nums2:
    sum += num
    
print(sum)