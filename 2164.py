class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd_indices = []  
        even_indices = []

        for i, number in enumerate(nums):
            if i % 2:
                odd_indices.append(nums[i])
            else:
                even_indices.append(nums[i])

        odd_indices.sort(reverse=True)
        even_indices.sort()

        result = []
        even_index = 0
        odd_index = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(even_indices[even_index])
                even_index += 1
            else:
                result.append(odd_indices[odd_index])
                odd_index += 1
        
        return result