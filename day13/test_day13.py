import day13code
from day13code import test_input


def test_order_comparer():

    left = [1,1,3,1,1]
    right = [1,1,5,1,1]
    assert day13code.correct_order_comparer(left, right) == True

    left = [1,1,5,1,1]
    right = [1,1,3,1,1]
    assert day13code.correct_order_comparer(left, right) == False

    left = [[1],[2,3,4]]
    right = [[1],4]
    assert day13code.correct_order_comparer(left, right) == True
    
    left = [[1],4]
    right = [[1],[2,3,4]]
    assert day13code.correct_order_comparer(left, right) == False

    left = [9]
    right = [[8,7,6]]
    assert day13code.correct_order_comparer(left, right) == False
    
    left = [[8,7,6]]
    right = [9]
    assert day13code.correct_order_comparer(left, right) == True

    left = [[4,4],4,4]
    right = [[4,4],4,4,4]
    assert day13code.correct_order_comparer(left, right) == True
    
    left = [[4,4],4,4,4]
    right = [[4,4],4,4]
    assert day13code.correct_order_comparer(left, right) == False

    left = [7,7,7,7]
    right = [7,7,7]
    assert day13code.correct_order_comparer(left, right) == False
    
    left = [7,7,7]
    right = [7,7,7,7]
    assert day13code.correct_order_comparer(left, right) == True

    left = []
    right = [3]
    assert day13code.correct_order_comparer(left, right) == True
    
    left = [3]
    right = []
    assert day13code.correct_order_comparer(left, right) == False

    left = [[[]]]
    right = [[]]
    assert day13code.correct_order_comparer(left, right) == False
    
    left = [[]]
    right = [[[]]]
    assert day13code.correct_order_comparer(left, right) == True

    left = [1,[2,[3,[4,[5,6,7]]]],8,9]
    right = [1,[2,[3,[4,[5,6,0]]]],8,9]
    assert day13code.correct_order_comparer(left, right) == False
    
    left = [1,[2,[3,[4,[5,6,0]]]],8,9]
    right = [1,[2,[3,[4,[5,6,7]]]],8,9]
    assert day13code.correct_order_comparer(left, right) == True

    left = [[3, [7], [0], 7]]
    right = [[5, 2]]
    assert day13code.correct_order_comparer(left, right) == True

    left = [5, 6, 6, 7, 3]
    right = [5, 6, 6, 7]
    assert day13code.correct_order_comparer(left, right) == False

    left = [[7, 6, 5], [9, 1]]
    right = [[[3, 2, [1, 0, 9, 2, 7], 4, 2], [[4, 10, 3, 4], 6, [0, 4]], [], [9, [1, 0], []]], [], [5, [4, [4, 10, 9, 6, 3], 3], [[8, 2, 8], [10, 7, 7, 1], 10, [], 5], [9], 9], [0, 7, 3, 5, 10]]
    assert day13code.correct_order_comparer(left, right) == False

    left = [[[0, 4], [[10, 8, 6, 3], 7], 3], [], [[], [[2, 5, 3], [], [6, 7, 10, 7], 5, 7]], [5, 9, [[], [4, 3], 3, [1, 4, 3]], 3], [10, 5, 3, 5, [9, 2, [9, 9], 10, [3, 8, 9, 8, 5]]]]
    right = [[[6, 2, [8, 2, 4, 6]], [9, 6, [], []], [2, [9, 7, 8], [8, 8, 5, 7], [6, 7, 0, 10]], [[0, 7]], 8], [[[6], [9], 1], [[], 5]], [[7, 0, [4, 8], 10], 5, 7, 8]]
    assert day13code.correct_order_comparer(left, right) == True

# def test_part_1_answer_finder():
#     input = test_input
#     assert day13code.part_1_answer_finder(input) == 13