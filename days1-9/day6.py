import re
input = 'day6input.txt'

def read_message():
    f = open(input)

    content = f.read()

    return content

message = read_message()

for idx, char in enumerate(message):
    group = set(message[idx:idx + 14])
    if len(group) == 14:
        print(idx + 14)
        break