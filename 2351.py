class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = {}

        for letter in s:
            if letter not in d:
                d[letter] = 1
            else:
                return letter
        
        return ""