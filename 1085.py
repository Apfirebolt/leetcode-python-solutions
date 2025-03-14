def sumOfDigits(nums):
    min_num = min(nums)
    result = 0

    while min_num:
        r = min_num % 10
        result += r
        min_num //= 10
    
    print('Result:', result)

    if result % 2 == 0:
        result = 1

    return result
        

nums = [34,23,1,24,75,33,54,8]
print(sumOfDigits(nums))

nums = [99,77,33,66,55]
print(sumOfDigits(nums))