# Max average sub-array

def findMaxAverage(nums, k):
        
    current_sum = sum(nums[:k])
    max_sum = current_sum

    for i in range(k, len(nums)):
        # i joins the window and i-k leaves the window
        current_sum += nums[i] - nums[i - k]  # Update the sum
        max_sum = max(max_sum, current_sum)
    
    return max_sum / k


arr = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage(arr, k))