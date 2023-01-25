def solution_one(nums: list[int]) -> int:
    num_set = set(nums)
    max_seq = 0
    for num in nums:
        length = 0
        if num - 1 not in num_set:
            while num + length in num_set:
                length += 1
            if length > max_seq:
                max_seq = length
    return max_seq
