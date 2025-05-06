def removeVowels(s):
    result = ''

    for letter in s:
        if letter in 'aeiou':
            continue
        result += letter

    return letter


s = "leetcodeisacommunityforcoders"
print(removeVowels(s))