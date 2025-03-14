def splitWordsBySeparator(words, separator):
    result = []
    for word in words:
        current_words = word.split(separator)
        for nested_word in current_words:
            if nested_word:
                result.append(nested_word)

    return result

words = ["$easy$","$problem$"]
separator = "$"

print(splitWordsBySeparator(words, separator))