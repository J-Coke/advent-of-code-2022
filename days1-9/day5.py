import re
input = 'day5input.txt'
def read_piles():
    f = open(input)

    content = f.read()

    piles_moves = re.split('\n\n', content)
    
    return piles_moves[0].split('\n')

def read_moves():
    f = open(input)

    content = f.read()

    piles_moves = re.split('\n\n', content)
    
    moves = re.split('\n', piles_moves[1])

    return moves

def split_moves(move):
    # print(move)
    split_move = re.split('\D+', move)
    return split_move[1:]

piles = read_piles()
moves = list(map(split_moves, read_moves()))
# print(moves)
piles_dict = {}
def piles_dict_creator(piles):
    for pile in piles[:-1]:
        for idx, char in enumerate(pile):
            if char.isalpha():
                if idx not in piles_dict.keys():
                    piles_dict[idx] = []
                piles_dict[idx] += char
piles_dict_creator(piles)
# print(piles_dict)
def mover(moves, piles_dict):
    for move in moves[:-1]:
        # print(move)
        move[0] = int(move[0])
        popped = piles_dict[int(move[1]) * 4 - 3][0:move[0]]
        del piles_dict[int(move[1]) * 4 - 3][0:move[0]]
        print(popped, piles_dict)
        piles_dict[int(move[2]) * 4 - 3] = popped + piles_dict[int(move[2]) * 4 - 3]
    sorted_piles = dict(sorted(piles_dict.items()))
    top_crates = ''
    for pile in sorted_piles:
        # print(pile, "pile")
        top_crates += sorted_piles[pile][0]
    return top_crates
print(mover(moves, piles_dict))