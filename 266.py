class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = {}

        for letter in s:
            d[letter] = d.get(letter, 0) + 1
        
        odd_count = 0
        for num in d.values():
            if num % 2:
                odd_count += 1
        
        if len(s) % 2:
            return odd_count == 1
        else:
            return odd_count == 0
        
        return True