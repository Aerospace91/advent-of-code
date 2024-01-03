lines = open('input.txt').read().splitlines()

total_sum = 0
for line in lines:
    game_id = int(line.split(':')[0][5:])
    games = line.split(':')[1].split(';')
    
    is_valid = True
    for game in games:
        game = game.strip().split(',')
        # color_dict = {'red': 0, 'green': 0, 'blue': 0}
        for color in game:
            color_dict = {'red': 0, 'green': 0, 'blue': 0}
            color = color.strip().split(' ')
            for i in range(0, len(color), 2):
                color_dict[color[i + 1]] = int(color[i])
            if color_dict.get('green') > 13:
                is_valid = False
            if color_dict['red'] > 12:
                is_valid = False
            if color_dict['blue'] > 14:
                is_valid = False
    if is_valid:
        total_sum += game_id
            
print(total_sum)