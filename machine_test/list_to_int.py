def solution_one(nums: list[int]) -> int:
    position = 1
    total = 0

    for num in nums[::-1]:
        total += position * num
        position *= 10

    return total
