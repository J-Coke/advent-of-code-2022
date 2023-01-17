import ast

with open('input.txt', "r") as input:
    full_list = input.read().split('\n\n')

with open('test-input.txt', "r") as test_input:
    test_list = test_input.read().split('\n\n')

def input_formatter(input):
    left_right_input = [lr.split('\n') for lr in input]

    for topidx, signal in enumerate(left_right_input):
        for bottomidx, side in enumerate(signal):
            left_right_input[topidx][bottomidx] = ast.literal_eval(side)
    return left_right_input

test_input = input_formatter(test_list)
full_input = input_formatter(full_list)

def value_comparer(left, right):
        if isinstance(left, list) and isinstance(right, list):
            if len(left) == 0:
                return True
            elif len(right) == 0:
                return False
        for index, (left_value, right_value) in enumerate(zip(left, right)):
            if type(left_value) != type(right_value):
                if isinstance(left_value, int):
                    left[index] = [left_value]
                    return value_comparer(left, right)
                elif isinstance(right_value, int):
                    right[index] = [right_value]
                    return value_comparer(left, right)
            if isinstance(left_value, list) and isinstance(right_value, list):
                global correct_order
                correct_order = value_comparer(left_value, right_value)
            if left_value > right_value:
                correct_order = False
                return correct_order
            elif left_value < right_value:
                return True
            elif index == len(right) - 1 and index != len(left) - 1:
                return False
        return correct_order

def correct_order_comparer(left, right):
    global correct_order
    correct_order = True
    
    return value_comparer(left, right)

def part_1_answer_finder(input):
    count = 1
    wrong = 0
    total = 0
    all = 0
    for signal in input:
        if correct_order_comparer(signal[0], signal[1]):
            total += count
            # print(count, total)
        else:
            wrong += count
            # print(signal[0])
            # print(signal[1])
            # print('\n')
            # print(wrong)
        all += count    
        count += 1
    return total

print('Part 1: ', part_1_answer_finder(full_input))

with open('input.txt', "r") as input:
    full_list = input.read().split('\n')

with open('test-input.txt', "r") as test_input:
    test_list = test_input.read().split('\n')

def input_formatter(input):

    formatted_input = []

    for signal in input:
        if len(signal) > 0:
            formatted_input.append(ast.literal_eval(signal))
    return formatted_input

test_input = input_formatter(test_list)
full_input = input_formatter(full_list)
global ordered_signals
ordered_signals = [[[2]], [[6]]]
twoidx = 0
sixidx = 1

def signal_sorter(input):
    unsorted_list = input
    for unsortedidx, signal in enumerate(unsorted_list):
        for idx, sig in enumerate(ordered_signals):
            if value_comparer(signal, sig):
                global twoidx
                global sixidx
                if idx <= twoidx:
                    twoidx += 1
                    sixidx += 1
                elif idx <= sixidx:
                    sixidx += 1
                ordered_signals.insert(idx, signal)
                signal_sorter(unsorted_list[unsortedidx + 1:])
                break
            elif idx == len(ordered_signals) - 1:
                ordered_signals.append(signal)
                signal_sorter(unsorted_list[unsortedidx + 1:])
                break
            else:
                continue
        break
    return (twoidx + 1) * (sixidx + 1)

print('Part 2: ', signal_sorter(full_input))
