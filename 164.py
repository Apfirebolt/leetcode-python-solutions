# Max gaps

def maximumGap(nums):
    if len(nums) < 2:
        return 0

    max_gap = 0
    nums.sort()
    for i in range(1, len(nums)):
        max_gap = max(max_gap, nums[i] - nums[i-1])

    return max_gap