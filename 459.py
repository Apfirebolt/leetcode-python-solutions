# Repeated sub-string pattern

# def repeatedSubstringPattern(s):
#     return s in (s + s)[1:-1]

# Compare this snippet from 459.py:

def repeatedSubstringPattern(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    for key, value in d.items():
        if value == 1:
            return False
        
    return True


s = "abab"
print(repeatedSubstringPattern(s)) # True