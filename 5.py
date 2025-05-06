# Longest palindrome sub-string

def longest_palindrome(s):
    left = 0
    right = 0

    while left < len(s) and right < len(s):
        if s[left] == s[right]:
            right += 1
        else:
            left += 1
            right = left

    return s[left:right]

print(longest_palindrome("babad")) # bab
print(longest_palindrome("abacdfgdcaba")) # abacdfgdcaba