class Solution:
    def numSquares(self, n: int) -> int:
        # dp 背包问题
        # o(n* sqrt(n)) z(sqrt(n))
        nums = [i*i for i in range(int(n**0.5)+1)]
        dp = [0] + [float('inf')]*n
        
        for num in nums:
            for j in range(num, n+1):
                dp[j] = min(dp[j], dp[j-num]+1)
        
        return dp[-1]
        