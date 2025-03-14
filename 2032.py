class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)

        count = {}

        for number in set1:
            count[number] = count.get(number, 0) + 1
        for number in set2:
            count[number] = count.get(number, 0) + 1
        for number in set3:
            count[number] = count.get(number, 0) + 1
        
        result = [num for num, cnt in count.items() if cnt >= 2]
        return result
