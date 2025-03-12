def canThreePartsEqualSum(arr):
    total_sum = sum(arr)
    count = 0

    if total_sum % 3:
        return False

    target_sum = total_sum / 3
    current_sum = 0

    for number in arr:
        current_sum += number
        if current_sum == target_sum:
            count += 1
            current_sum = 0
    
    return count >= 3