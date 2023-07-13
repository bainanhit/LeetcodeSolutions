class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # dp优化时间复杂度
        # O(KN) Z(KN)
        # 状态定义：dp[i][j] 表示前 i 个数的数组中正好有 j 个逆序对的个数；
        res = 0
        mod = 1000000007
        # dp[i][j] = dp[i-1][j] + dp[i-1][j-1] + ... + dp[i-1][j-i-1]
        # dp[i][j-1] =            dp[i-1][j-1] + ... + dp[i-1][j-1-(i-1-1)] + dp[i-1][j-1-(i-1)]
        # dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1-i-1]
        dp = [[0]*(k+1) for _ in range(n+1)]
        dp[1][0] = 1
        for i in range(2, n+1):
            # 边界
            bound = min(k, int(i*(i-1)/2))
            for j in range(0, bound+1):
                dp[i][j] = ((dp[i][j-1] if j>=1 else 0) + 
                            dp[i-1][j] - (dp[i-1][j-i] if j>=i else 0)) % mod
        
        res = dp[n][k]
        return res
