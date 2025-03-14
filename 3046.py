class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        if max(d.values()) > 2:
            return False
        
        return True