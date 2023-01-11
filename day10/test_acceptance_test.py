import day10code

with open('./inputs/day10-test-input.txt', "r") as test_input:
    test_list = test_input.read().split('\n')

def test_final_result_test():
    assert day10code.signal_strength_sum(test_list) == 13140
