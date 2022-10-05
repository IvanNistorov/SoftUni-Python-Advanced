first_player, second_player = input().split(', ')

size = 6
maze = []
rest_for_first_player = 0
rest_for_second_player = 0

for _ in range(size):
    maze_elements = input().split()
    maze.append(maze_elements)

while True:
    coordinates = input().strip("()")
    row_move, col_move = [int(x) for x in coordinates.split(", ")]

    position = maze[row_move][col_move]

    if rest_for_first_player > 0:
        rest_for_first_player -= 1
        first_player, second_player = second_player, first_player
        rest_for_first_player, rest_for_second_player = rest_for_second_player, rest_for_first_player
        continue

    if position == "E":
        print(f"{first_player} found the Exit and wins the game!")
        break
    elif position == "T":
        print(f"{first_player} is out of the game! The winner is {second_player}.")
        break
    elif position == "W":
        print(f"{first_player} hits a wall and needs to rest.")
        first_player, second_player = second_player, first_player
        rest_for_first_player, rest_for_second_player = rest_for_second_player, rest_for_first_player
        rest_for_second_player += 1
        continue

    first_player, second_player = second_player, first_player
    rest_for_first_player, rest_for_second_player = rest_for_second_player, rest_for_first_player
