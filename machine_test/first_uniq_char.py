

def solution_one(string: str) -> int:
    counter = {}

    for c in string:
        counter[c] = counter.get(c, 0) + 1

    for index, char in enumerate(string):
        if string[char] == 1:
            return index

    return -1


def solution_two(string: str) -> int:
    for index, char in enumerate(string):
        if string.count(char) == 1:
            return index
    return -1
