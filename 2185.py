# leetcode 2185 - counting words with a given prefix

def prefixCount(words, prefix):
    count = 0
    for word in words:
        if word.startswith(prefix):
            count += 1
    return count


words = ["dog", "deer", "deal"]
prefix = "de"

print(prefixCount(words, prefix)) # 2
