def at_least_k_distance_away(nums, k):
    try:
        first_one_index = nums.index(1)
    except ValueError:
        return True

    for i in range(first_one_index+1, len(nums)):
        if nums[i] == 1:
            if i - first_one_index <= k:
                return False
            first_one_index = i
    
    return True


nums = [1,0,0,0,1,0,0,1]
k = 2

print(at_least_k_distance_away(nums, k))