def next_position(row, col, direction):
    if direction == "up":
        return row - 1, col
    elif direction == "down":
        return row + 1, col
    elif direction == "left":
        return row, col - 1
    elif direction == 'right':
        return row, col + 1


size = 6
field = []
rover_row = 0
rover_col = 0

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "E":
            rover_row = row
            rover_col = col
    field.append(row_elements)

while True:
    commands = input().split(', ')
    rover_row, rover_col = next_position(rover_row, rover_col, commands)
