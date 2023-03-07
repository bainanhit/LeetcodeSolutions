class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0
        # dp[i][0] 表示第i天持有股票所得现金
        # dp[i][1] 表示第i天不持有股票所得最多现金
        # 第i-1天就持有股票，那么就保持现状，所得现金就是昨天持有股票的所得现金 即：dp[i - 1][0]
        # 第i天买入股票，所得现金就是昨天不持有股票的所得现金减去 今天的股票价格 即：dp[i - 1][1] - prices[i]
        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][0] = -(prices[0])
        dp[0][1] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        
        return dp[-1][1]