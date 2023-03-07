class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        if n <= 1:
            return 1
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
    
        for i in range(3, n+1):
            for j in range(0, n):
                dp[i] += dp[j] * dp[i-j-1]

        return dp[n]
                
       