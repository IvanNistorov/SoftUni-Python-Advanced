def prize_won(sum):
    if 100 <= sum < 200:
        return "Football"
    elif 200 <= sum < 300:
        return "Teddy Bear"
    elif 300 <= sum:
        return "Lego Construction Set"


def inside_board(row, col):
    if 0 <= row < 6 and 0 <= col < 6:
        return True


hits_history = []
points = 0
board = []

for _ in range(6):
    row_elements = [int(x) if x != "B" and x != "В" else x for x in input().split()]
    board.append(row_elements)

for _ in range(3):
    temp = input().replace("(", "")
    temp = temp.replace(")", "")

    temp = list(map(int, temp.split(", ")))
    hit_row, hit_col = temp

    if (hit_row, hit_col) in hits_history:
        continue

    if inside_board(hit_row, hit_col):
        if board[hit_row][hit_col] == "B":
            for i in range(6):
                if i == hit_row:
                    continue
                points += board[i][hit_col]
            hits_history.append((hit_row, hit_col))

if prize_won(points):
    print(f"Good job! You scored {points} points, and you've won {prize_won(points)}.")
else:
    print(f"Sorry! You need {100 - points} points more to win a prize.")