class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = -1

        for sentence in sentences:
            sentence_list = sentence.strip().split(' ')
            max_words = max(max_words, len(sentence_list))
        
        return max_words