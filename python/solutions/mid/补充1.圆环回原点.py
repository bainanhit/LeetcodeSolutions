# 题目：圆环上有10个点，编号为0~9。
# 从0点出发，每次可以逆时针和顺时针走一步，问走n步回到0点共有多少种走法
class Solution:
    def backToOrigin(self,n):
        # 走n步到0的方案数=走n-1步到1的方案数+走n-1步到9的方案数
        dp = [[0]*n for _ in range(n+1)]
        dp[0][0] = 1
        # dp[i][j]为从0点出发走i步到j点的方案数
        length = 10
        for i in range(1, n+1):
            for j in range(n):
                dp[i][j] = dp[i-1][(j-1+length)%length] + dp[i-1][(j+1)%length]

        return dp[n][0]
        