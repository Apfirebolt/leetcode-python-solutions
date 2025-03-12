# Count elements

def count_elements(arr):
    result = 0
    d = {}
    for number in arr:
        d[number] = d.get(number, 0) + 1
        
    for number in d:
        if number + 1 in d:
            result += d[number]
    
    return result


arr = [1, 2, 3]
print(count_elements(arr))

