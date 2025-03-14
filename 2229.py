def isConsecutive(nums):
    min_value = min(nums)
    max_value = min_value + len(nums) - 1

    current = min_value
    while current < max_value:
        current += 1
        if current not in nums:
            return False
    
    return True


def isConsecutiveBetter(nums):
    min_value = min(nums)
    max_value = max(nums)

    return max_value - min_value + 1 == len(nums) == len(set(nums))
        


nums = [1,3,4,2]
print(isConsecutive(nums))