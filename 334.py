class Solution:
    def increasingTriplet(self, nums):
        first_min = float('inf')
        second_min = float('inf')

        for num in nums:  # Changed arr[i] to num for clarity and correctness
            if num <= first_min:
                first_min = num
            elif num <= second_min:
                second_min = num
            else:
                return True

        return False