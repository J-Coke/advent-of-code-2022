import re

with open('input.txt', "r") as input:
    full_list = input.read().split('\n')

with open('test-input.txt', "r") as test_input:
    test_list = test_input.read().split('\n')

def input_formatter(input):
    return [list(map(int, re.split('Sensor at x=|, y=|: closest beacon is at x=', line)[1:])) for line in input]

formatted_test = input_formatter(test_list)
formatted_full = input_formatter(full_list)

def sensor_and_beacon_mapper(input, line_of_interest):
    x_bounds = [0, 0]

    for line in input:
        if line[0] < x_bounds[0]:
            x_bounds[0] = line[0]
        if line[0] > x_bounds[1]:
            x_bounds[1] = line[0]
        if line[2] < x_bounds[0]:
            x_bounds[0] = line[2]
        if line[2] > x_bounds[1]:
            x_bounds[1] = line[2]

    resulting_line = ['.'] * (x_bounds[1] - x_bounds[0] + 1)

    for line in input:
        in_range = (abs(line[2] - line[0]) + abs(line[3] - line[1])) - abs(line[1] - line_of_interest)
        if in_range >= 0:
            while in_range >= 0:
                if line[0] + in_range - x_bounds[0] > x_bounds[1]:
                    resulting_line += ['.'] * (line[0] + in_range - x_bounds[0] - x_bounds[1])
                    x_bounds[1] = line[0] + in_range - x_bounds[0]
                if line[0] - in_range < x_bounds[0]:
                    resulting_line = ['.'] * (x_bounds[0] - (line[0] - in_range)) + resulting_line
                    x_bounds[0] = line[0] - in_range
                resulting_line[line[0] + in_range - x_bounds[0]] = '#'
                resulting_line[line[0] - in_range - x_bounds[0]] = '#'
                in_range -= 1

    for line in input:
        if line[3] == line_of_interest:
            resulting_line[line[2] - x_bounds[0]] = 'B'

    return resulting_line.count('#')

print('Part 1: ', sensor_and_beacon_mapper(formatted_full, 2000000))

def dark_spot_finder(input, xy_limit):
    topright = set()
    bottomright = set()
    bottomleft = set()
    topleft = set()

    for line in input:
        mandist = abs(line[2] - line[0]) + abs(line[3] - line[1])
        x = line[0]
        y = line[1] - mandist - 1
        while y < line[1]:
            topright.add((x,y))
            x += 1
            y += 1
        while x > line[0]:
            bottomright.add((x,y))
            x -= 1
            y += 1
        while y > line[1]:
            bottomleft.add((x,y))
            x -= 1
            y -= 1
        while x < line[0]:
            topleft.add((x,y))
            x += 1
            y -= 1
    darkcoords = list(topright.intersection(bottomright, bottomleft, topleft))
    (dark_x, dark_y) = darkcoords[0]
    return dark_x * xy_limit + dark_y

print('Part 2: ', dark_spot_finder(formatted_full, 4000000))
