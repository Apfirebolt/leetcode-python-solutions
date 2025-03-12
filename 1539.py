# Kth missing positive integer

def findKthPositive(arr, k):
    i = 1
    while k > 0:
        if i not in arr:
            k -= 1
        i += 1
    return i - 1


arr = [2, 3, 4, 7, 11]
k = 5
print(findKthPositive(arr, k))