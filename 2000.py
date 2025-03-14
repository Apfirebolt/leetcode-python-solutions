def reversePrefix(word, ch: str):
    try:
        first_index = word.index(ch)
    except ValueError:
        return word

    reversed = word[:first_index+1][::-1]
    remaining = word[first_index + 1:]

    return reversed + remaining