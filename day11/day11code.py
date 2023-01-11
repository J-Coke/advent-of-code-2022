import math
import re

with open('input.txt', "r") as input:
    full_list = input.read().split('\n')[0:-1]

with open('test-input.txt', "r") as test_input:
    test_list = test_input.read().split('\n')

def operation(old, operator, num):
    if num == 'old':
        num = int(old)
    else:
        num = int(num)
    old = int(old)
    if operator == '*':
        new = old * num
    elif operator == '+':
        new = old + num
    return new

def divisible_test(numerator, divisor):
    if numerator % divisor == 0:
        return True
    else:
        return False

# class Monkey:
#     def __init__(self, items, operation, test, action)

input = test_list

monkeys = {}

def item_map_function(item):
    if item[-1] == ',':
        return int(item[:-1])
    else:
        return int(item)

def monkey_dict_creator(input):
    monkey_num = "0"
    current_monkey = f"Monkey {monkey_num}"
    for line in input:
        if line[0:4] == "Monk":
            monkey_num = line.split(' ')[1][:-1]
            current_monkey = f"Monkey {monkey_num}"
            monkeys[current_monkey] = {}
        if re.search("Star", line):
            line_split = line.split()[2:]
            # print(line_split, 'ls')
            item_list = list(map(item_map_function, line_split))
            monkeys[current_monkey]['items'] = item_list
        if re.search("Oper", line):
            line_split = line.split()
            monkeys[current_monkey]['operation'] = {}
            monkeys[current_monkey]['operation']['operator'] = line_split[-2]
            monkeys[current_monkey]['operation']['num'] = line_split[-1]
        if re.search("Test", line):
            line_split = line.split()
            monkeys[current_monkey]['test-divisor'] = line_split[-1]
        if re.search("true", line):
            line_split = line.split()
            monkeys[current_monkey]['if-true'] = line_split[-1]
        if re.search("false", line):
            line_split = line.split()
            monkeys[current_monkey]['if-false'] = line_split[-1]
            monkeys[current_monkey]['inspections'] = 0
    return monkeys

monkey_dict = monkey_dict_creator(input)
# print(monkey_dict)
def round(monkey_dict):
    for monkey in monkey_dict.items():
        while len(monkey[1]['items']) > 0:
            stress_value = monkey[1]['items'][0]
            # print(monkey[0], stress_value)
            operator = monkey[1]['operation']['operator']
            num = monkey[1]['operation']['num']
            monkey[1]['inspections'] += 1
            stress_value = operation(stress_value, operator, num)
            # print(monkey[0], stress_value)
            stress_value = math.floor(stress_value / 3)
            # print(monkey[0], stress_value)
            item_to_throw = monkey[1]['items'].pop(0)
            receiver = ''
            if divisible_test(stress_value, int(monkey[1]['test-divisor'])):
                receiver = monkey[1]['if-true']
            else:
                receiver = monkey[1]['if-false']
            monkey_dict[f'Monkey {receiver}']['items'].append(stress_value)
            # print(monkey[0], monkey_dict[monkey[0]]['items'])
            # break
        # break
    return monkey_dict
        # while len(monkey[items])

def game(monkey_dict, rounds_to_play):
    games_left = rounds_to_play - 1
    monkey_dict = round(monkey_dict)
    if games_left == 0:
        return monkey_dict
    else:
        return game(monkey_dict, games_left)

monkey_dict = game(monkey_dict, 20)
# print(monkey_dict)
def monkey_business_calculator(monkey_dict):
    active_monkeys = [0]
    for monkey in monkey_dict.items():
        if monkey[1]['inspections'] > active_monkeys[0]:
            active_monkeys.insert(0, monkey[1]['inspections'])
        elif monkey[1]['inspections'] > active_monkeys[1]:
            active_monkeys.insert(1, monkey[1]['inspections'])
    return active_monkeys[0] * active_monkeys[1]

part_1_answer = monkey_business_calculator(monkey_dict)

print('Part 1: ', part_1_answer)