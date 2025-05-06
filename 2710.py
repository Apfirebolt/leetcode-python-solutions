def removeTrailingZeros(num: str) -> str:
    result = ''
    i = len(num)-1

    while i > -1:
        if num[i] != '0':
            break
        i -= 1
    
    return num[:i+1]


s = '51230100'
print(removeTrailingZeros(s)) # 512301

