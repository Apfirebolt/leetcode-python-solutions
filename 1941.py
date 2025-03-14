def areOccurrencesEqual(s: str) -> bool:
    d = {}
    for letter in s:
        d[letter] = d.get(letter, 0) + 1
    
    return len(set(d.values())) == 1


s = "abacbc"
print(areOccurrencesEqual(s))
        