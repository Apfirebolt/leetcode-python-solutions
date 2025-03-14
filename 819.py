def maxOccurences(paragraph, banned):
    paragraph.split("//W+")
    print(paragraph)


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(maxOccurences(paragraph.split(), banned)) # ball