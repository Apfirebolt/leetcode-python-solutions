class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        start = 0
        end = len(nums) // 2
        result = []

        is_first = True

        while start < len(nums) // 2:
            if is_first:
                result.append(nums[start])
                start += 1
                is_first = False
            else:
                result.append(nums[end])
                end += 1
                is_first = True
        
        result.append(nums[len(nums)-1])
        
        return result
        