# 2 sum problem

def two_sum(arr, target):

    d = {}
    for number in range(len(arr)):
        if target - arr[number] in d:
            return [number, d[target-arr[number]]]
        d[arr[number]] = number

    return -1


nums, target = [2,7,11,15], 9

print(two_sum(nums, target))

