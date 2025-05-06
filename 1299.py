def replaceElements(arr):
    if not arr:  # Handle empty array case
        return []

    n = len(arr)
    max_right = -1  # Initialize max_right to -1 (for the last element)

    for i in range(n - 1, -1, -1):  # Iterate from right to left
        temp = arr[i]  # Store the current element
        arr[i] = max_right  # Replace the current element with max_right
        max_right = max(max_right, temp)  # Update max_right if necessary

    return arr

print(replaceElements([17, 18, 5, 4, 6, 1])) # [18, 6, 6, 6, 1, -1]