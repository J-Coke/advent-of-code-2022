import ast

with open('input.txt', "r") as input:
    full_list = input.read().split('\n\n')

with open('test-input.txt', "r") as test_input:
    test_list = test_input.read().split('\n\n')

def input_formatter(input):
    left_right_input = [lr.split('\n') for lr in input]

    for topidx, signal in enumerate(left_right_input):
        for bottomidx, side in enumerate(signal):
            # print(side)
            left_right_input[topidx][bottomidx] = ast.literal_eval(side)
    return left_right_input

test_input = input_formatter(test_list)
full_input = input_formatter(full_list)

def correct_order_comparer(left, right):
    print('called', left, right)
    global correct_order
    correct_order = True
    count = 0
    # if count == 0:
    #     if len(left) > len(right):
    #         return False
    #     else:
    #         count = 1
    def value_comparer(left, right):
        print(left, right, 'line 32')
        if isinstance(left, list) and isinstance(right, list):
            if len(left) == 0:
                return True
            elif len(right) == 0:
                return False
        for index, (left_value, right_value) in enumerate(zip(left, right)):
            print(index, left_value, right_value, '24')
            if type(left_value) != type(right_value):
                # print(isinstance(right_value, int))
                if isinstance(left_value, int):
                    left[index] = [left_value]
                    # print(left, right, "29")
                    return value_comparer(left, right)
                elif isinstance(right_value, int):
                    right[index] = [right_value]
                    # print(left, right, "32")
                    return value_comparer(left, right)
            if isinstance(left_value, list) and isinstance(right_value, list):
                print(left_value, right_value, value_comparer(left_value, right_value), '35')
                global correct_order
                correct_order = value_comparer(left_value, right_value)
            # print(left_value, right_value, '37')
            if left_value > right_value:
                correct_order = False
                return correct_order
            elif left_value < right_value:
                return True
            elif index == len(right) - 1 and index != len(left) - 1:
                return False
            # elif index == len(right) - 1 and index == len(left) - 1:
        return correct_order
    return value_comparer(left, right)

def part_1_answer_finder(input):
    print(len(input))
    count = 1
    wrong = 0
    total = 0
    all = 0
    for signal in input:
        print(count, total, wrong, all, "start for")
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