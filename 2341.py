# Max pairs leftover

# Input: nums = [1,3,2,1,3,2,2]
# Output: [3,1]

def max_pairs(nums):
    d = {}
    pairs = 0

    i = 0
    while i < len(nums):
        num = nums[i]
        if num not in d:
            d[num] = i
            i += 1
        else:
            # remove both occurrences of the pair
            del nums[i]
            del nums[d[num]]
            pairs += 1
            # reset the dictionary and index
            d = {}
            i = 0
    
    return [pairs, len(nums)]

nums = [1,3,2,1,3,2,2]
print(max_pairs(nums)) # [3, 1]