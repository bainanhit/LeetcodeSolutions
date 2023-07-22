class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]
    
    # 优化空间复杂度: O(N) Z(1)
    def climbStairs(self, n: int) -> int:
        # Z(1)
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0, 1, 2]
        tmp = 0
        for i in range(3, n+1):
            tmp = dp[1] + dp[2]
            dp[1] = dp[2]
            dp[2] = tmp

        return dp[-1]
    
    # fu: 一步有1,2..m个台阶
    def climbStairs(self, n: int, m:int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                if i >= j:
                    dp[i] += dp[i-j]
        
        return dp[-1]

