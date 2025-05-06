# Number complement

def findComplement(num):
    """
    :type num: int
    :rtype: int
    """
    # return int(''.join(['1' if i == '0' else '1' for i in bin(num)[2:]]), 2)
    return int(''.join(['1' if i == '0' else '0' for i in bin(num)[2:]]), 2)




print(findComplement(5)) # 2