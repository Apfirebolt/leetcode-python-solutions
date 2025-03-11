class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        result = -1
        nums.sort()

        left = 0
        right = len(nums)-1

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum < k:
                result = max(current_sum, result)
                left += 1
            else:
                right -= 1
        
        return result