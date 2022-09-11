def solution_one(string_a: str, string_b: str) -> bool:
    if len(string_a) != len(string_b):
        return False

    return sorted(string_a) == sorted(string_b)


def solution_two(string_a: str, string_b: str) -> bool:
    if len(string_a) != len(string_b):
        return False

    for char_a, char_b in zip(string_a, string_b):
        if char_a not in string_b or char_b not in string_a:
            return False

    return True


def solution_three(string_a: str, string_b: str) -> bool:
    pass
