# Hamming distance between two integers

def hammingDistance(x, y):
    xor = x ^ y
    count = 0
    while xor:
        count += xor & 1
        xor >>= 1
    return count


print(hammingDistance(1, 4)) # 2
