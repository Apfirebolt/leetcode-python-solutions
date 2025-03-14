def kidsWithCandies(candies, extraCandies):
    max_candy = max(candies)
    result = [False] * len(candies)

    for i in range(len(candies)):
        if candies[i] + extraCandies >= max_candy:
            result[i] = True
    
    return result


candies = [2,3,5,1,3]
extraCandies = 3

print(kidsWithCandies(candies, extraCandies))