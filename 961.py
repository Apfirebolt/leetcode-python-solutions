class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                if d[num] >= 2:
                    return num
                d[num] += 1
        
        for key, value in d.items():
            if value >= 2:
                return key
            
        