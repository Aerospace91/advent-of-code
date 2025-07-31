user_input = open('input.txt').read()
# user_input = '^>v<'

visited_coordinates = {}

x, y, x2, y2 = 0, 0, 0, 0
delivered = 0
count = 0

def track_coordinates(x, y):
    coordinate = (x, y)
    if coordinate in visited_coordinates:
        visited_coordinates[coordinate] += 1
    else:
        visited_coordinates[coordinate] = 1


track_coordinates(x, y)
for direction in user_input:
    count += 1
    if direction == '>':
        if count % 2 == 0:
            x += 1
            track_coordinates(x, y)
        else:
            x2 += 1
            track_coordinates(x2, y2)
    if direction == '<':
        if count % 2 == 0:
            x -= 1
            track_coordinates(x, y)
        else:
            x2 -= 1
            track_coordinates(x2, y2)
    if direction == '^':
        if count % 2 == 0:
            y += 1
            track_coordinates(x, y)
        else:
            y2 += 1
            track_coordinates(x2, y2)
    if direction == 'v':
        if count % 2 == 0:
            y -= 1
            track_coordinates(x, y)
        else:
            y2 -= 1
            track_coordinates(x2, y2)

print(len(visited_coordinates))