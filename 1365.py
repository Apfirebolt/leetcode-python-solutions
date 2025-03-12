def smallerNumbersThanCurrent(nums):
    
    # Create a copy of the array
    sorted_nums = sorted(nums)
    
    # Create a dictionary to store the number of elements smaller than the current element
    count = {}
    
    # Loop through the sorted array
    for i, num in enumerate(sorted_nums):
        if num not in count:
            count[num] = i
    
    # Loop through the original array
    for i, num in enumerate(nums):
        nums[i] = count[num]
    
    return nums



arr = [8, 1, 2, 2, 3]
print(smallerNumbersThanCurrent(arr))  # [4, 0, 1, 1, 3]