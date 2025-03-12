class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_count = 0
        start = 0
        end = k-1
        vowels = ['a', 'e', 'i', 'o', 'u']

        while end < len(s):
            current_count = 0
            for i in range(start, end+1):
                if s[i] in vowels:
                    current_count += 1
            
            max_count = max(current_count, max_count)
            end += 1
            start += 1

        return max_count


def maxVowels(self, s: str, k: int) -> int:
    max_count = 0
    current_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in range(k):
        if s[i] in vowels:
            current_count += 1
        
    max_count = max(current_count, max_count)

    for i in range(k, len(s)):
        # new element enters the windo
        if s[i] in vowels:
            current_count += 1
        # element leaving the window    
        if s[i-k] in vowels:
            current_count -= 1
    
        max_count = max(current_count, max_count)

    return max_count