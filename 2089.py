def targetIndices(nums, target):
    nums.sort()
    result = []
    for i, num in enumerate(nums):
        if num == target:
            result.append(i)
    
    return result


nums = [1,2,5,2,3]
target = 2

print(targetIndices(nums, target))