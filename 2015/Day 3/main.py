user_input = open('input.txt').read()
# user_input = '^>v<'

visited_coordinates = {}

x, y = 0, 0
delivered = 0

def track_coordinates(x, y):
    coordinate = (x, y)
    if coordinate in visited_coordinates:
        visited_coordinates[coordinate] += 1
    else:
        visited_coordinates[coordinate] = 1


track_coordinates(x, y)
for direction in user_input:
    if direction == '>':
        x += 1
        track_coordinates(x, y)
    if direction == '<':
        x -= 1
        track_coordinates(x, y)
    if direction == '^':
        y += 1
        track_coordinates(x, y)
    if direction == 'v':
        y -= 1
        track_coordinates(x, y)

print(len(visited_coordinates))