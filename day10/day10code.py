import math

with open('./inputs/day10input.txt', "r") as input:
    list = input.read().split('\n')[0:-1]

with open('./inputs/day10-test-input.txt', "r") as test_input:
    test_list = test_input.read().split('\n')[0:-1]

def instruction_reader(instruction_line):
    value = [1, 0]
    if instruction_line != 'noop':
        value = [2, int(instruction_line.split()[1])]
        
    return value

def signal_strength_sum(input):
    cycle = 1
    x = 1
    sum = 0
    stored_instructions = []
    for n in range(220):
        instruction = 'noop'
        if n < len(input):
            instruction = input[n]
            stored_instructions.append(instruction_reader(instruction))
        if (cycle - 20) / 40 % 1 == 0:
            sum += cycle * x
        # if instruction_reader(instruction):
        #     stored_instructions.append(instruction_reader(instruction))
        if len(stored_instructions) > 0:
            stored_instructions[0][0] -= 1
            if stored_instructions[0][0] == 0:
                x += stored_instructions[0][1]
                stored_instructions.pop(0)
        print("end of: ", cycle,'x = ', x, instruction, sum, stored_instructions)
        cycle += 1

        
        
    return sum

def show_screen(input):
    cycle = 1
    x = 1
    stored_instructions = []
    screen = [[], [], [], [], [], []]
    for n in range(240):
        row = math.floor((cycle - 1) / 40)
        row_position = cycle - row * 40 - 1
        instruction = 'noop'
        if n < len(input):
            instruction = input[n]
            stored_instructions.append(instruction_reader(instruction))
        
        print(x - 2, row_position, x + 2)
        if x - 2 < row_position < x + 2:
            screen[row].append('#')
        else:
            screen[row].append('.')
        if len(stored_instructions) > 0:
            stored_instructions[0][0] -= 1
            if stored_instructions[0][0] == 0:
                x += stored_instructions[0][1]
                stored_instructions.pop(0)
        cycle += 1

    for row in screen:
        print(''.join(row))
        
    # return sum

print(show_screen(list))