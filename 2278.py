class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        import math
        word_count = s.count(letter)

        return math.floor((word_count / len(s)) * 100)