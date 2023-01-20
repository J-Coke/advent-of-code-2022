with open('input.txt', "r") as input:
    full_list = input.read().split('\n')

with open('test-input.txt', "r") as test_input:
    test_list = test_input.read().split('\n')

def input_formatter(input):
    return [[list(map(int, num.split(','))) for num in line.split(' -> ')] for line in input]

formatted_test = input_formatter(test_list)
formatted_full = input_formatter(full_list)

def rock_map_creator(input):
    rock_map = [['+']]
    lrboundary = [500, 500]
    bottomboundary = 0
    for lineidx, line in enumerate(input):
        for pointidx, point in enumerate(line):
            if point[0] < lrboundary[0]:
                for idx, map_line in enumerate(rock_map):
                    rock_map[idx] = ['.'] * (lrboundary[0] - point[0]) + map_line
                lrboundary[0] = point[0]
            if point[0] > lrboundary[1]:
                for idx, map_line in enumerate(rock_map):
                    rock_map[idx] = map_line + ['.'] * (point[0] - lrboundary[1])
                lrboundary[1] = point[0]
            if point[1] > bottomboundary:
                rock_map += (point[1] - bottomboundary) * [(['.'] * (lrboundary[1] - lrboundary[0] + 1))]
                bottomboundary = point[1]
    current_position = [input[0][0][0] - lrboundary[0], input[0][0][1]]
    for lineidx, line in enumerate(input):
        current_position = [line[0][0], line[0][1]]
        rock_map[current_position[1]][current_position[0] - lrboundary[0]] = '#'
        for pointidx, point in enumerate(line):
            while point != current_position:
                if point[0] - current_position[0] < 0:
                    current_position[0] -= 1
                    rock_map[current_position[1]][current_position[0] - lrboundary[0]] = '#'
                if point[0] - current_position[0] > 0:
                    current_position[0] += 1
                    rock_map[current_position[1]][current_position[0] - lrboundary[0]] = '#'
                if point[1] - current_position[1] < 0:
                    current_position[1] -= 1
                    rock_map[current_position[1]][current_position[0] - lrboundary[0]] = '#'
                if point[1] - current_position[1] > 0:
                    current_position[1] += 1
                    rock_map[current_position[1]][current_position[0] - lrboundary[0]] = '#'

    return rock_map

test_rock_map = rock_map_creator(formatted_test)
full_rock_map = rock_map_creator(formatted_full)

def particle_place_finder(map, lineidx, position):
    if lineidx == len(map) - 1 or position == 0 or position == len(map[0]) + 1:
        return 'end'
    elif map[lineidx + 1][position] == '.':
        return particle_place_finder(map, lineidx + 1, position)
    elif map[lineidx + 1][position - 1] != '.':
        if map[lineidx + 1][position + 1] != '.':
            return [lineidx, position]
        else:
            return particle_place_finder(map, lineidx + 1, position + 1)
    else:
        return particle_place_finder(map, lineidx + 1, position - 1)

count = 0
def sand_dropper(rock_and_sand_map):
    global count
    count += 1
    rock_and_sand_map
    source_idx = rock_and_sand_map[0].index('+')
    
    for idx, line in enumerate(rock_and_sand_map[1:]):
        if rock_and_sand_map[idx + 1][source_idx] != '.':
            new_place = particle_place_finder(rock_and_sand_map, idx, source_idx)
            if new_place == 'end':
                return count - 1
            else:
                rock_and_sand_map[new_place[0]][new_place[1]] = 'o'
                return sand_dropper(rock_and_sand_map)
    

print('Part 1: ', sand_dropper(full_rock_map))

def particle_place_finder_2(map, lineidx, position):
    if position == 0:
        return 'left'
    if position == len(map[0]) - 1:
        return 'right'
    if lineidx == len(map) - 1 or position == len(map[0]) - 1:
        return 'end'
    elif map[lineidx + 1][position] == '.':
        return particle_place_finder_2(map, lineidx + 1, position)
    elif map[lineidx + 1][position - 1] != '.':
        if map[lineidx + 1][position + 1] != '.':
            return [lineidx, position]
        else:
            return particle_place_finder_2(map, lineidx + 1, position + 1)
    else:
        return particle_place_finder_2(map, lineidx + 1, position - 1)

count = 0

test_rock_map += [(['.'] * len(test_rock_map[0]))]
test_rock_map += [(['#'] * len(test_rock_map[0]))]
full_rock_map += [(['.'] * len(full_rock_map[0]))]
full_rock_map += [(['#'] * len(full_rock_map[0]))]

def sand_dropper_2(rock_and_sand_map, count, limit):
    if count == limit:
        return rock_and_sand_map
    count += 1
    if rock_and_sand_map[0].count('+') == 0:
        sand = 0
        for idx, line in enumerate(rock_and_sand_map):
            sand += line.count('o')
        return sand
    source_idx = rock_and_sand_map[0].index('+')
    for idx, line in enumerate(rock_and_sand_map[1:]):
        if rock_and_sand_map[idx + 1][source_idx] != '.':
            new_place = particle_place_finder_2(rock_and_sand_map, idx, source_idx)
            if new_place == 'end':
                break
            elif new_place == 'left':
                for idx, map_line in enumerate(rock_and_sand_map):
                    rock_and_sand_map[idx] = ['.'] + map_line
                rock_and_sand_map[-1][0] = '#'
                count -= 1
                return sand_dropper_2(rock_and_sand_map, count, limit)
            elif new_place == 'right':
                for idx, map_line in enumerate(rock_and_sand_map):
                    rock_and_sand_map[idx] = map_line + ['.']
                rock_and_sand_map[-1][-1] = '#'
                count -= 1
                return sand_dropper_2(rock_and_sand_map, count, limit)
            else:
                rock_and_sand_map[new_place[0]][new_place[1]] = 'o'
                return sand_dropper_2(rock_and_sand_map, count, limit)

def recur(map, start, finish):
    result = sand_dropper_2(map, start, finish)
    if isinstance(result, int):
        return result
    else:
        return recur(map, finish, finish + 800)

print('Part 2: ', recur(full_rock_map, 0, 800))
