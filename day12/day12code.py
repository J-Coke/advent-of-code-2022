import math
import re

with open('input.txt', "r") as input:
    full_list = input.read().split('\n')[0:-1]

with open('test-input.txt', "r") as test_input:
    test_list = test_input.read().split('\n')

input = full_list

def convert_to_ints(input):
    int_map = [[ord(j) for j in i] for i in input]
    return int_map

converted_input = convert_to_ints(input)
# for line in converted_input:
#     print(line)

def start_end_finder(numerical_map):
    start_end = [[0, 0], [0, 0]]
    for row_ind, row in enumerate(numerical_map):
        for col_ind, col in enumerate(row):
            if col == 83: start_end[0] = [row_ind, col_ind] 
            if col == 69: start_end[1] = [row_ind, col_ind]
    return start_end

start_end = start_end_finder(converted_input)

# print(start_end)

def fewest_steps_from_end_finder(converted_input, start_end):
    end_row = start_end[1][0]
    end_col = start_end[1][1]
    start_row = start_end[0][0]
    start_col = start_end[0][1]
    current_spot_row = 0
    current_spot_col = 0
    fewest_steps_grid = [['' for j in i] for i in converted_input]
    fewest_steps_grid[end_row][end_col] = 0
    fewest_steps_grid[start_row][start_col] = 'X'
    converted_input[end_row][end_col] = 123
    # if converted_input[end_row - 1][end_col] == 122:
    #     current_spot_row = end_row - 1
    #     current_spot_col = end_col
    # if converted_input[end_row + 1][end_col] == 122:
    #     current_spot_row = end_row + 1
    #     current_spot_col = end_col
    # if converted_input[end_row][end_col - 1] == 122:
    #     # print('here')
    #     current_spot_row = end_row
    #     current_spot_col = end_col - 1
    # if converted_input[end_row][end_col + 1] == 122:
    #     current_spot_row = end_row
    #     current_spot_col = end_col + 1
    # fewest_steps_grid[current_spot_row][current_spot_col] = ['-', 1]
    # routes_to_current = []
    # current_level = 122
    test_lim = 5000
    while test_lim > 0:
        for rowidx, row in enumerate(converted_input):
            for letteridx, letter in enumerate(row):

                current = fewest_steps_grid[rowidx][letteridx]
                if current == 'X':
                    continue
                if rowidx != 0:
                    if converted_input[rowidx - 1][letteridx] >= letter - 1 and current != '' and fewest_steps_grid[rowidx - 1][letteridx] == '':
                        # print("pot", fewest_steps_grid[rowidx - 1][letteridx], 'curr', current)
                        fewest_steps_grid[rowidx - 1][letteridx] = current + 1
                #         fewest_steps_grid[current_spot_row - 1][current_spot_col][1] = fewest_steps_grid[current_spot_row][current_spot_col][1] + 1
                #         # print("in 1", [print(line) for line in fewest_steps_grid])
                #         routes_to_current.append([current_spot_row - 1, current_spot_col])
                # print(current_spot_row < len(converted_input) - 1)
                if rowidx < len(converted_input) - 1:
                    if converted_input[rowidx + 1][letteridx] >= converted_input[rowidx][letteridx] - 1 and current != '' and fewest_steps_grid[rowidx + 1][letteridx] == '':
                        fewest_steps_grid[rowidx + 1][letteridx] = current + 1
                if letteridx != 0:
                    if converted_input[rowidx][letteridx - 1] >= converted_input[rowidx][letteridx] - 1 and current != '' and fewest_steps_grid[rowidx][letteridx - 1] == '':
                        fewest_steps_grid[rowidx][letteridx - 1] = current + 1
                #     if converted_input[current_spot_row][current_spot_col - 1] >= current_level - 1 and fewest_steps_grid[current_spot_row][current_spot_col - 1][0] != '-':
                #         print('3')
                #         fewest_steps_grid[current_spot_row][current_spot_col - 1][1] = fewest_steps_grid[current_spot_row][current_spot_col][1] + 1
                #         routes_to_current.append([current_spot_row, current_spot_col - 1])
                # # print("before 4", current_spot_col, len(converted_input[0]))
                if letteridx < len(converted_input[0]) - 1:
                    if converted_input[rowidx][letteridx + 1] >= letter - 1 and current != '' and fewest_steps_grid[rowidx][letteridx + 1] == '':
                        fewest_steps_grid[rowidx][letteridx + 1] = current + 1
                #     if converted_input[current_spot_row][current_spot_col + 1] >= current_level - 1 and fewest_steps_grid[current_spot_row][current_spot_col + 1][0] != '-':
                #         print('4')
                #         fewest_steps_grid[current_spot_row][current_spot_col + 1][1] = fewest_steps_grid[current_spot_row][current_spot_col][1] + 1
                #         routes_to_current.append([current_spot_row, current_spot_col + 1])

    # while fewest_steps_grid[start_row][start_col][0] == '.':
        # print("start while", current_spot_row, current_spot_col, fewest_steps_grid)
        # if current_spot_row != 0:
        #     if converted_input[current_spot_row - 1][current_spot_col] >= current_level - 1  and fewest_steps_grid[current_spot_row - 1][current_spot_col][0] != '-':
        #         fewest_steps_grid[current_spot_row - 1][current_spot_col][1] = fewest_steps_grid[current_spot_row][current_spot_col][1] + 1
        #         print("in 1", [print(line) for line in fewest_steps_grid])
        #         routes_to_current.append([current_spot_row - 1, current_spot_col])
        # # print(current_spot_row < len(converted_input) - 1)
        # if current_spot_row < len(converted_input) - 1:
        #     if converted_input[current_spot_row + 1][current_spot_col] >= current_level - 1 and fewest_steps_grid[current_spot_row + 1][current_spot_col][0] != '-':
        #         print('2')
        #         fewest_steps_grid[current_spot_row + 1][current_spot_col][1] = fewest_steps_grid[current_spot_row][current_spot_col][1] + 1
        #         routes_to_current.append([current_spot_row + 1, current_spot_col])
        # if current_spot_col != 0:
        #     if converted_input[current_spot_row][current_spot_col - 1] >= current_level - 1 and fewest_steps_grid[current_spot_row][current_spot_col - 1][0] != '-':
        #         print('3')
        #         fewest_steps_grid[current_spot_row][current_spot_col - 1][1] = fewest_steps_grid[current_spot_row][current_spot_col][1] + 1
        #         routes_to_current.append([current_spot_row, current_spot_col - 1])
        # # print("before 4", current_spot_col, len(converted_input[0]))
        # if current_spot_col < len(converted_input[0]) - 1:
        #     if converted_input[current_spot_row][current_spot_col + 1] >= current_level - 1 and fewest_steps_grid[current_spot_row][current_spot_col + 1][0] != '-':
        #         print('4')
        #         fewest_steps_grid[current_spot_row][current_spot_col + 1][1] = fewest_steps_grid[current_spot_row][current_spot_col][1] + 1
        #         routes_to_current.append([current_spot_row, current_spot_col + 1])
        # for route in routes_to_current:
        #     # print('route', route)
        #     current_spot_row = route[0]
        #     current_spot_col = route[1]
        #     fewest_steps_grid[current_spot_row][current_spot_col][0] = '-'
        #     current_level = converted_input[current_spot_row][current_spot_col]
        # # if len(routes_to_current) == 1:
        # #     current_spot_row = routes_to_current[0][0]
        # #     current_spot_col = routes_to_current[0][1]
        # #     fewest_steps_grid[current_spot_row][current_spot_col][0] = '-'
        # #     current_level = converted_input[current_spot_row][current_spot_col]
        # # print('routes', routes_to_current)
        # routes_to_current = []

        test_lim -= 1
    # print("here",[print(line) for line in fewest_steps_grid])
    min_path = min(fewest_steps_grid[start_row - 1][start_col] + 1, fewest_steps_grid[start_row][start_col + 1] + 1, fewest_steps_grid[start_row + 1][start_col] + 1)


    return fewest_steps_grid

fewest_steps_grid = fewest_steps_from_end_finder(converted_input, start_end)

def min_path_from_S_finder(fewest_steps_grid, start_end):
    start_row = start_end[0][0]
    start_col = start_end[0][1]
    min_path = min(fewest_steps_grid[start_row - 1][start_col] + 1, fewest_steps_grid[start_row][start_col + 1] + 1, fewest_steps_grid[start_row + 1][start_col] + 1)
    return min_path
# print([print(line) for line in fewest_steps_from_end_finder(converted_input, start_end)])
print('Part 1: ',  min_path_from_S_finder(fewest_steps_grid, start_end))
# print('Part 1: ', part_1_answer)
def nearest_a(fewest_steps_grid, converted_input):
    min = 383
    for rowidx, i in enumerate(converted_input):
        for colidx, j in enumerate(i):
            if j == 97:
                if fewest_steps_grid[rowidx][colidx] != '':
                    if fewest_steps_grid[rowidx][colidx] < min:
                        min = fewest_steps_grid[rowidx][colidx]
    return min


print('Part 2: ', nearest_a(fewest_steps_grid, converted_input))