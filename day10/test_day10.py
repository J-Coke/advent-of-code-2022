import day10code


with open('./inputs/day10-test-input.txt', "r") as test_input:
    test_list = test_input.read().split('\n')[0:-1]

with open('./inputs/small-test.txt', "r") as small_test_input:
    small_test_list = small_test_input.read().split('\n')

def test_instruction_reader():
    assert day10code.instruction_reader('noop') == [1, 0]
    assert day10code.instruction_reader('addx 2') == [2, 2]
    assert day10code.instruction_reader('addx -11') == [2, -11]


def test_twentieth_cycle():
    assert day10code.signal_strength_sum(test_list[:20]) == 420

def test_sixtyeth_cycle():
    assert day10code.signal_strength_sum(test_list[:60]) == 1560

