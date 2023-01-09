def read():
    f = open('rucksacks.txt', 'r')

    content = f.read()

    rucksack_array = content.split('\n')

    return rucksack_array

rucksack_array = read()

def char_valuer(char):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96

def splitter(array):
    for i in range(0, len(array), 3):
        yield array[i:i + 3]

def find_badge(rucksack_array):
    team_array = list(splitter(rucksack_array))
    total = 0
    for team in team_array:
        for char in team[0]:
            if char in team[1] and char in team[2]:
                total += char_valuer(char)
                # print(rucksack, char, total)
                break
    return total

print(find_badge(rucksack_array))