# Roman to integer

def convertRomanToInteger(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    
    for i in range(len(roman)-1, -1, -1):
        if i == len(roman) - 1:
            result = roman_dict[roman[i]]
        else:
            if roman_dict[roman[i]] < roman_dict[roman[i+1]]:
                result -= roman_dict[roman[i]]
            else:
                result += roman_dict[roman[i]]
    
    return result



# Test cases
print(convertRomanToInteger("MCMXCIV"))