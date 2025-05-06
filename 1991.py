class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        right_sum = total_sum

        for i in range(len(nums)):
            right_sum -= nums[i]

            if left_sum == right_sum:
                return i
            
            left_sum += nums[i]
        
        return -1
        