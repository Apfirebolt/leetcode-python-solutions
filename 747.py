# def dominantIndex(nums):
#     second = nums[0]
#     largest = max(nums)

#     for i in range(1, len(nums)):
#         if nums[i] > second and nums[i] != largest:
#             second = nums[i]
    
#     if largest >= second * 2:
#         return nums.index(largest)
#     else:
#         return -1


def dominantIndex(nums):
    second = nums[0]
    largest = max(nums)

    for i in range(1, len(nums)):
        if nums[i] > second and nums[i] != largest:
            second = nums[i]
    
    if largest >= second * 2:
        return nums.index(largest)
    else:
        return -1
    

print(dominantIndex([3, 6, 1, 0])) # 1
print(dominantIndex([1, 2, 3, 4])) # -1