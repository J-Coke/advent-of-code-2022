import itertools
from itertools import filterfalse 
import re

def read():
    f = open('day4input.txt')

    content = f.read()

    move_array = re.split('\s', content)

    return move_array[:-1]
# print(read())

raw_list = read()
# raw_item = '98-99,3-97'
def filter_for_contained(raw_item):
    split_item = re.split("\D", raw_item)
    # print(split_item)
    item_pairs = [[int(split_item[0]), int(split_item[1])], [int(split_item[2]), int(split_item[3])]]
    poss_container = 0
    containee = 1
    # print(item_pairs)
    if max(item_pairs[0]) == max(item_pairs[1]):
        return True
    if max(item_pairs[0]) < max(item_pairs[1]):
        poss_container = 1
        containee = 0
    if min(item_pairs[poss_container]) <= min(item_pairs[containee]):
        # print(min(item_pairs[poss_container]), min(item_pairs[containee]))
        return True

filtered_for_contained = filter(filter_for_contained, raw_list)
the_rest = filterfalse(filter_for_contained, raw_list)
# print(len(list(filtered_for_contained)))
# print(len(list(the_rest)))

def filter_for_overlap(raw_item):
    split_item = re.split("\D", raw_item)
    # print(split_item)
    item_pairs = [[int(split_item[0]), int(split_item[1])], [int(split_item[2]), int(split_item[3])]]
    higher_pair = 0
    lower_pair = 1
    # print(item_pairs)
    if max(item_pairs[0]) < max(item_pairs[1]):
        higher_pair = 1
        lower_pair = 0
    if min(item_pairs[higher_pair]) <= max(item_pairs[lower_pair]):
        # print(min(item_pairs[poss_container]), min(item_pairs[containee]))
        return True

fitered_for_overlap = filter(filter_for_overlap, raw_list)

print(len(list(fitered_for_overlap)))