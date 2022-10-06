def sums(row, col, current_field):
    result = 0
    if current_field == "D":
        result = (board[0][col] + board[-1][col] + board[row][0] + board[row][-1]) * 2
        return result
    elif current_field == "T":
        result = (board[0][col] + board[-1][col] + board[row][0] + board[row][-1]) * 3
        return result
    elif current_field == "B":
        result = 501
        return result
    else:
        result = current_field
        return result


def is_inside(row, col, s):
    return 0 <= row < s and 0 <= col < s


size = 7
first, second = input().split(", ")
first_player_points = 501
second_player_points = 501
first_player_throws = 0
second_player_throws = 0
board = []

for _ in range(size):
    board_elements = [int(x) if x != "D" and x != "T" and x != "B" else x for x in input().split()]
    board.append(board_elements)

while first_player_points > 0 and second_player_points > 0:
    coordinates = input().strip()
    row_hit, col_hit = [int(x) for x in coordinates.split(", ")]

    if is_inside(row_hit, col_hit, size):
        field = board[row_hit][col_hit]
        total = sums(row_hit, col_hit, field)
        first_player_throws += 1
        first_player_points -= total
    else:
        first_player_throws += 1

    first, second = second, first
    first_player_points, second_player_points = second_player_points, first_player_points
    first_player_throws, second_player_throws = second_player_throws, first_player_throws

first, second = second, first
first_player_points, second_player_points = second_player_points, first_player_points
first_player_throws, second_player_throws = second_player_throws, first_player_throws
print(f"{first} won the game with {first_player_throws} throws!")
