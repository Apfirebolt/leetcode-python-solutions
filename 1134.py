# Armstrong number

def is_armstrong_number(n):
    digit_sum = 0
    k = len(str(n))

    digits = list(str(n))

    for digit in digits:
        digit_sum += int(digit) ** k
    
    return digit_sum == n


print(is_armstrong_number(153))