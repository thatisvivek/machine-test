def solution_one(string: str) -> bool:
    return string == string[::-1]


def solution_two(string: str) -> bool:
    i = 0
    j = len(string) - 1

    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1

    return True
