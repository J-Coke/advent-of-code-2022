import day10code
 


# from day10 import signal_strength_sum

# sys.path.append( '/inputs' )
# import 'day10-test-input.txt' as input
with open('./inputs/day10-test-input.txt', "r") as test_input:
    test_list = test_input.read().split('\n')

def test_final_result_test():
    assert day10code.signal_strength_sum(test_list) == 13140

# print(signal_strength_sum(test_list))