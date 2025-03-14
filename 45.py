# Jump game 2

def jump(nums):
    n = len(nums)

    if n == 1:
        return 0
    
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(n):
        for j in range(i+1, min(i+nums[i]+1, n)):
            dp[j] = min(dp[j], dp[i] + 1)
    
    return dp[-1]