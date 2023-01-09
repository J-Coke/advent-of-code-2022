file = 'moves_H.txt'

def read(file):
    f = open(file, 'r')

    content = f.read()

    move_array = content.split('\n')

    return move_array

moves = read(file)

def tail_dir_finder(old, new):
    result = ''
    if new[0] > old[0]:
        if new[1] > old[1]:
            result = 'DR'
        if new[1] == old[1]:
            result = 'D'
        if new[1] < old[1]:
            result = 'DL'
    if new[0] == old[0]:
        if new[1] > old[1]:
            result = 'R'
        if new[1] < old[1]:
            result = 'L'
    if new[0] < old[0]:
        if new[1] > old[1]:
            result = 'UR'
        if new[1] == old[1]:
            result = 'U'
        if new[1] < old[1]:
            result = 'UL'
    return result

def mover(moves, knot):
    # print("knot: ", knot, '\n', moves)
    grid = [["s"]]
    head_position = [0, 0]
    tail_position = [0, 0]
    old_tail_position = tail_position.copy()
    next_knot_move_list = [['X']]
    # print(next_knot_move_list)
    for move in moves:
        # [print(line) for line in grid]
        # print(next_knot_move_list, head_position, tail_position, move)
        # print(move[0])
        if move[0:2] == "R ":
            count = int(move[2:])
            while count > 0:
                if len(grid[head_position[0]]) - 1 <= head_position[1]:
                    grid = [sub + ["."] for sub in grid]
                head_position[1] += 1
                count -= 1
                # print(head_position, tail_position, "head tail R")
                if head_position[1] - tail_position[1] > 1:
                    # print(old_tail_position, tail_position, "oldnew")
                    tail_position[1] += 1
                    if tail_position[0] > head_position[0]:
                        tail_position[0] -= 1
                    elif tail_position[0] < head_position[0]:
                        tail_position[0] += 1
                    # print(head_position, tail_position,tail_position[0] < head_position[0], "tail")
                    grid[tail_position[0]][tail_position[1]] = "#"
                    # print(old_tail_position, tail_position, tail_dir_finder(old_tail_position, tail_position))
                    if next_knot_move_list[-1][0] == tail_dir_finder(old_tail_position, tail_position):
                        next_knot_move_list[-1][1] += 1
                    else:
                        if tail_dir_finder(old_tail_position, tail_position):
                            next_knot_move_list.append([tail_dir_finder(old_tail_position, tail_position), 1])
                    old_tail_position = tail_position.copy()
                # print(head_position, tail_position, "after")
            continue
        if move[0:2] == "UR":
            count = int(move[2:])
            # print(head_position, tail_position, "head tail UR")
            while count > 0:
                if len(grid[head_position[0]]) - 1 <= head_position[1]:
                    grid = [sub + ["."] for sub in grid]
                if head_position[0] == 0:
                    times = len(grid[0])
                    grid.insert(0, ["."] * times)
                    tail_position[0] += 1
                    head_position[0] += 1
                    old_tail_position[0] += 1
                head_position[1] += 1
                head_position[0] -= 1
                count -= 1
                # print(count, head_position, tail_position, "head tail UR etx")
                if head_position[1] - tail_position[1] > 1:
                    tail_position[1] += 1
                    if head_position[0] < tail_position[0]:
                        tail_position[0] -= 1
                elif tail_position[0] - head_position[0] > 1:
                    tail_position[0] -= 1
                    if head_position[1] > tail_position[1]:
                        tail_position[1] += 1
                if next_knot_move_list[-1][0] == tail_dir_finder(old_tail_position, tail_position):
                        next_knot_move_list[-1][1] += 1
                else:
                    if tail_dir_finder(old_tail_position, tail_position):
                        next_knot_move_list.append([tail_dir_finder(old_tail_position, tail_position), 1])
                grid[tail_position[0]][tail_position[1]] = "#"
                old_tail_position = tail_position.copy()
                # print(head_position, tail_position, "after")
            continue
        if move[0:2] == "U ":
            count = int(move[2:])
            # print(head_position, tail_position, "head tail U")
            while count > 0:
                if head_position[0] == 0:
                    times = len(grid[0])
                    grid.insert(0, ["."] * times)
                    old_tail_position[0] += 1
                    tail_position[0] += 1
                    head_position[0] += 1
                head_position[0] -= 1
                count -= 1
                # print(count, head_position, tail_position, "head tail U etx")
                if tail_position[0] - head_position[0] > 1:
                    tail_position[0] -= 1
                    if tail_position[1] > head_position[1]:
                        tail_position[1] -= 1
                    elif tail_position[1] < head_position[1]:
                        tail_position[1] += 1
                    # print(count, head_position, tail_position, "head tail U inif")
                    # print(head_position, tail_position,tail_position[0] < head_position[0], "tail")
                    grid[tail_position[0]][tail_position[1]] = "#"
                    # print(old_tail_position, tail_position, tail_dir_finder(old_tail_position, tail_position))
                    if next_knot_move_list[-1][0] == tail_dir_finder(old_tail_position, tail_position):
                        next_knot_move_list[-1][1] += 1
                    else:
                        if tail_dir_finder(old_tail_position, tail_position):
                            next_knot_move_list.append([tail_dir_finder(old_tail_position, tail_position), 1])
                    old_tail_position = tail_position.copy()
                # print(head_position, tail_position, "after")
            continue
        if move[0:2] == "UL":
            count = int(move[2:])
            # print(head_position, tail_position, "head tail UL")
            while count > 0:
                if head_position[0] == 0:
                    times = len(grid[0])
                    grid.insert(0, ["."] * times)
                    tail_position[0] += 1
                    head_position[0] += 1
                    old_tail_position[0] += 1
                if head_position[1] == 0:
                    grid = [["."] + sub for sub in grid]
                    # print(grid)
                    tail_position[1] += 1
                    head_position[1] += 1
                    old_tail_position[1] += 1
                head_position[0] -= 1
                head_position[1] -= 1
                count -= 1
                # print(count, head_position, tail_position, "head tail UL etx")
                if tail_position[1] - head_position[1] > 1:
                    tail_position[1] -= 1
                    if head_position[0] < tail_position[0]:
                        tail_position[0] -= 1
                elif tail_position[0] - head_position[0] > 1:
                    tail_position[0] -= 1
                    if head_position[1] < tail_position[1]:
                        tail_position[1] -= 1
                # print(next_knot_move_list[-1], old_tail_position, tail_position, tail_dir_finder(old_tail_position, tail_position), "direction")
                if next_knot_move_list[-1][0] == tail_dir_finder(old_tail_position, tail_position):
                        next_knot_move_list[-1][1] += 1
                else:
                    if tail_dir_finder(old_tail_position, tail_position):
                        next_knot_move_list.append([tail_dir_finder(old_tail_position, tail_position), 1])
                grid[tail_position[0]][tail_position[1]] = "#"
                old_tail_position = tail_position.copy()
                # print(head_position, tail_position, "after")
            continue
        if move[0] == "L":
            count = int(move[2:])
            # print(head_position, tail_position, "head tail")
            while count > 0:
                if head_position[1] == 0:
                    grid = [["."] + sub for sub in grid]
                    # print(grid)
                    tail_position[1] += 1
                    head_position[1] += 1
                    old_tail_position[1] += 1
                head_position[1] -= 1
                count -= 1
                if tail_position[1] - head_position[1] > 1:
                    tail_position[1] -= 1
                    if tail_position[0] > head_position[0]:
                        tail_position[0] -= 1
                    elif tail_position[0] < head_position[0]:
                        tail_position[0] += 1
                    grid[tail_position[0]][tail_position[1]] = "#"
                    if next_knot_move_list[-1][0] == tail_dir_finder(old_tail_position, tail_position):
                        next_knot_move_list[-1][1] += 1
                    else:
                        if tail_dir_finder(old_tail_position, tail_position):
                            next_knot_move_list.append([tail_dir_finder(old_tail_position, tail_position), 1])
                    old_tail_position = tail_position.copy()
            continue
        if move[0:2] == "DL":
            count = int(move[2:])
            # print(head_position, tail_position, "head tail DL")
            while count > 0:
                if len(grid) - 1 <= head_position[0]:
                    times = len(grid[0])
                    grid.append(["."] * times)
                if head_position[1] == 0:
                    grid = [["."] + sub for sub in grid]
                    # print(grid)
                    tail_position[1] += 1
                    head_position[1] += 1
                    old_tail_position[1] += 1
                head_position[1] -= 1
                head_position[0] += 1
                count -= 1
                # print(count, head_position, tail_position, "head tail DL etx")
                if tail_position[1] - head_position[1] > 1:
                    tail_position[1] -= 1
                    if head_position[0] > tail_position[0]:
                        tail_position[0] += 1
                elif head_position[0] - tail_position[0] > 1:
                    tail_position[0] += 1
                    if head_position[1] < tail_position[1]:
                        tail_position[1] -= 1
                if next_knot_move_list[-1][0] == tail_dir_finder(old_tail_position, tail_position):
                        next_knot_move_list[-1][1] += 1
                else:
                    if tail_dir_finder(old_tail_position, tail_position):
                        next_knot_move_list.append([tail_dir_finder(old_tail_position, tail_position), 1])
                grid[tail_position[0]][tail_position[1]] = "#"
                old_tail_position = tail_position.copy()
                # print(head_position, tail_position, "after")
            continue
        if move[0:2] == "D ":
            count = int(move[2:])
            # print(head_position, tail_position, "head tail D")
            while count > 0:
                if len(grid) - 1 <= head_position[0]:
                    times = len(grid[0])
                    grid.append(["."] * times)
                head_position[0] += 1
                count -= 1
                if head_position[0] - tail_position[0] > 1:
                    tail_position[0] += 1
                    if tail_position[1] > head_position[1]:
                        tail_position[1] -= 1
                    elif tail_position[1] < head_position[1]:
                        tail_position[1] += 1
                    grid[tail_position[0]][tail_position[1]] = "#"
                    # print(old_tail_position, tail_position, tail_dir_finder(old_tail_position, tail_position))
                    if next_knot_move_list[-1][0] == tail_dir_finder(old_tail_position, tail_position):
                        next_knot_move_list[-1][1] += 1
                    else:
                        if tail_dir_finder(old_tail_position, tail_position):
                            next_knot_move_list.append([tail_dir_finder(old_tail_position, tail_position), 1])
                    old_tail_position = tail_position.copy()
                # print(head_position, tail_position, "after")
            continue
        if move[0:2] == "DR":
            count = int(move[2:])
            # print(head_position, tail_position, "head tail DR")
            while count > 0:
                if len(grid) - 1 <= head_position[0]:
                    times = len(grid[0])
                    grid.append(["."] * times)
                if len(grid[head_position[0]]) - 1 <= head_position[1]:
                    grid = [sub + ["."] for sub in grid]
                head_position[1] += 1
                head_position[0] += 1
                count -= 1
                # print(count, head_position, tail_position, "head tail DR etx")
                if head_position[1] - tail_position[1] > 1:
                    tail_position[1] += 1
                    if head_position[0] > tail_position[0]:
                        tail_position[0] += 1
                elif head_position[0] - tail_position[0] > 1:
                    tail_position[0] += 1
                    if head_position[1] > tail_position[1]:
                        tail_position[1] += 1
                if next_knot_move_list[-1][0] == tail_dir_finder(old_tail_position, tail_position):
                        next_knot_move_list[-1][1] += 1
                else:
                    if tail_dir_finder(old_tail_position, tail_position):
                        next_knot_move_list.append([tail_dir_finder(old_tail_position, tail_position), 1])
                grid[tail_position[0]][tail_position[1]] = "#"
                # [print(line) for line in grid]
                old_tail_position = tail_position.copy()
                # print(head_position, tail_position, "after")
            continue
    flat_grid = [element for sublist in grid for element in sublist]
    tail_count = flat_grid.count("#") + flat_grid.count("s")
    next_recursion_list = []
    # [print(line) for line in grid]
    print(tail_count)
    for step in next_knot_move_list[1:]:
        next_recursion_list.append(step[0] + ' ' + str(step[1]))
    if knot == 9:
        return tail_count
    else:
        mover(next_recursion_list, knot + 1)
            
print(mover(moves, 0))
# print(mover(read('moves_H.txt'), 0))