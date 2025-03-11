# remove duplicates from sorted array

def remove_duplicates(arr):
    i = 0
    j = 0

    while j < len(arr):
        if arr[i] != arr[j]:
            arr[i+1] = arr[j]
            i += 1
            j += 1
        else:
            j += 1

    return i+1


l = [1, 1, 2, 3, 4, 4, 5]
print(remove_duplicates(l))
