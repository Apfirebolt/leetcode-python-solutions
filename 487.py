def consecutive_ones(arr):
    max_count = float('-inf')
    current_count = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            copied_array = arr.copy()
            copied_array[i] = 1
            current_count = 0

            for j in range(len(copied_array)):
                if copied_array[j] == 1:
                    current_count += 1
                    max_count = max(max_count, current_count)
                else:
                    current_count = 0
        else:
            current_count += 1
            max_count = max(max_count, current_count)
    
    return max_count


def sliding_window_approach(arr):
    left = 0
    right = 0
    max_count = 0
    zero_count = 0

    while right < len(arr):
        if arr[right] == 0:
            zero_count += 1
        
        # move the window from the left
        while zero_count > 1:
            if arr[left] == 0:
                zero_count -= 1
            left += 1

        max_count = max(max_count, right - left + 1)
        right += 1
    
    return max_count
    

arr = [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
# print(consecutive_ones(arr))
print(sliding_window_approach(arr))