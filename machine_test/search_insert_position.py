def solution_one(nums: list[int], target: int) -> int:
    if target <= nums[0]:
        return 0
    elif target > nums[-1]:
        return len(nums)
    elif target == nums[-1]:
        return len(nums) - 1
    else:
        for idx, num in enumerate(nums):
            if num >= target:
                return idx


def solution_two(nums: list[int], target: int) -> int:
    for idx, num in enumerate(nums):
        if num >= target:
            return idx

        return len(nums)
