# Find closest to zero in an array

# Given an array of integers, find the number closest to zero. If there are two numbers that are equally close to zero, return the positive number.

def findClosest(nums):
    min_diff = float('inf')

    for i in range(len(nums)):
        if abs(nums[i]) < abs(min_diff):
            min_diff = nums[i]
        elif abs(nums[i]) == abs(min_diff):
            min_diff = max(min_diff, nums[i])
    
    return min_diff


nums = [-4,-2,1,4,8]
print(findClosest(nums))  # 1