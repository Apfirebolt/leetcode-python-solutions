# Longest palindrome length in a string

def longest_palindrome(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    odd = False
    length = 0
    for c in d:
        if d[c] % 2 == 0:
            length += d[c]
        else:
            length += d[c] - 1
            odd = True
    return length + 1 if odd else length