"""
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, 
causing the left and the right side of the deleted substring to concatenate together.
"""

# Remove adjacent duplicates from string

class Solution:
    def removeDuplicates(self, s, k):
        stack = []
        count = 0
        for letter in s:
            if stack and stack[-1][0] == letter:
                print(stack[-1][0], letter, stack)
                count = stack[-1][1] + 1
                stack.pop()
            else:
                count = 1
            if count < k:
                stack.append((letter, count))

        return ''.join([letter * count for letter, count in stack])
    

s = "deeedbbcccbdaa"
k = 3
print(Solution().removeDuplicates(s, k)) # Output: "aa"