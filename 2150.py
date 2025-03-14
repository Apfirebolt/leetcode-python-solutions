"""
You are given an integer array nums. A number x is lonely when it appears only once, and no adjacent numbers (i.e. x + 1 and x - 1) appear in the array.

Return all lonely numbers in nums. You may return the answer in any order.
"""


def lonelyNumbers(nums):
    d = {}

    for num in nums:
        d[num] = d.get(num, 0) + 1
    
    for num in nums:
        if num - 1 in d or num + 1 in d:
            d[num] = 0
    
    return [num for num in d if d[num] == 1]


nums = [1,2,3,4,5]
print(lonelyNumbers(nums))

nums = [1,1,1,1,1]
print(lonelyNumbers(nums))

nums = [1,2,3,4,5,6,7,8,9,10]
print(lonelyNumbers(nums))