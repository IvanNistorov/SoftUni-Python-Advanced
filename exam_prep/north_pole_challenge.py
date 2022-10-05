def moves(row, col, direction, steps):
    if direction == "up":
        return row - steps, col
    elif direction == "down":
        return row + steps, col
    elif direction == "left":
        return row, col - steps
    elif direction == 'right':
        return row, col + steps


def is_outside(row, col, row_num, col_num):
    return row < 0 or col < 0 or row >= row_num or col >= col_num


def reposition(row, col, row_number, col_number):
    if row < 0:
        return row_number - 1, col
    elif row >= row_number:
        return 0, col
    elif col < 0:
        return row, col_number - 1
    elif col >= col_number:
        return row, 0


row_number, col_number = [int(x) for x in input().split(', ')]

field = []
santa_row, santa_col = 0, 0
decorations = 0
gifts = 0
cookies = 0
items_counter = 0

for row in range(row_number):
    matrix_elements = input().split()
    for col in range(col_number):
        if matrix_elements[col] == "Y":
            santa_row, santa_col = row, col
        if matrix_elements[col] == "D" or matrix_elements[col] == "C" or matrix_elements[col] == "G":
            items_counter += 1
    field.append(matrix_elements)

line = input()

while line != "End":
    field[santa_row][santa_col] = "x"
    command_parts = line.split("-")
    command = command_parts[0]
    steps = int(command_parts[1])
    for _ in range(steps):

        santa_row, santa_col = moves(santa_row, santa_col, command, 1)
        if is_outside(santa_row, santa_col, row_number, col_number):
            santa_row, santa_col = reposition(santa_row, santa_col, row_number, col_number)

        if field[santa_row][santa_col] == "D":
            decorations += 1
            items_counter -= 1
            field[santa_row][santa_col] = "x"
        elif field[santa_row][santa_col] == "G":
            gifts += 1
            items_counter -= 1
            field[santa_row][santa_col] = "x"
        elif field[santa_row][santa_col] == "C":
            cookies += 1
            items_counter -= 1
            field[santa_row][santa_col] = "x"
        else:
            field[santa_row][santa_col] = "x"

        if items_counter <= 0:
            break

    if items_counter <= 0:
        print("Merry Christmas!")
        break

    line = input()
field[santa_row][santa_col] = "Y"
print("You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")
for row in field:
    print(*row, sep=' ')