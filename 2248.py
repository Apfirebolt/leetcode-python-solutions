# Leetcode 2248, common elements in multiple arrays

def common_elements(nums):
    d = {}
    for num in nums[0]:
        if num not in d:
            d[num] = 1

    
    for i in range(1, len(nums)):
        for num in nums[i]:
            if num in d:
                d[num] += 1
    
    # sort dictionary based on key
    d = dict(sorted(d.items(), key=lambda x: x[0]))
    result = []
    for key, value in d.items():
        if value == len(nums):
            result.append(key)
    
    return result
        


print(common_elements([[1, 2, 3], [2, 3, 4], [3, 4, 5]]))  # [3]
print(common_elements([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))