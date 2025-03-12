# Brute force approach

def arithmeticTriplets(nums, diff) -> int:
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[k] - nums[j] == diff and nums[j] - nums[i] == diff:
                    count += 1
    
    return count


# Time complexity: O(n^3)
# Space complexity: O(1)

# arr = [1, 2, 3, 4]
# diff = 1
# print(arithmeticTriplets(arr, diff))