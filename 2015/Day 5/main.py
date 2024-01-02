with open('input.txt') as f: lines = [line.strip() for line in f]
# lines = ['dvszwmarrgswjxmb']

vowels = ['a', 'e', 'i', 'o', 'u']
checks = ['ab', 'cd', 'pq', 'xy']

nice = 0

for line in lines:
    is_vowel = False
    is_double = False
    has_string = False
    count = 0
    for char in line:
            if char in vowels:
                count +=1
    if count >= 3:
        is_vowel = True
    for i in range(0, len(line) - 1):
        if line[i] == line[i + 1]:
            is_double = True
    for check in checks:
        if check in line:
            has_string = True
    if is_vowel and is_double and not has_string:
        nice += 1

print(nice)