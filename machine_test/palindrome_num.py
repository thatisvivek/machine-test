def solution_one(num: int) -> bool:
    if num < 0:
        return False

    rev_num = 0
    num_copy = num

    while num:
        r = num % 10
        rev_num = (rev_num * 10) + r
        num = num // 10

    return rev_num == num_copy
