class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        values = list(d.values())
        result = 0
        max_value = max(values)
        times = values.count(max_value)

        return max_value * times