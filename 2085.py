from collections import Counter
from typing import List

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1 = Counter(words1)
        count2 = Counter(words2)
        
        result = 0
        for word, freq in count1.items():
            if freq == 1 and count2.get(word, 0) == 1:
                result += 1
        return result