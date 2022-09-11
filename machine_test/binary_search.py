"""Binary search solutions"""


def solution(arr: list, num: int) -> int:
    """Binary search algorithm"""
    if not arr:
        return -1

    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        guess = arr[mid]

        if guess < num:
            left = mid + 1
        elif guess > num:
            right = mid - 1
        else:
            return guess

    return -1
