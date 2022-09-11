def solution_one(nums: list[int]) -> list[int]:
    for index, num in enumerate(nums):
        if index != num:
            nums[index], nums[num] = nums[num], nums[index]
            solution_one(nums)
    return nums
