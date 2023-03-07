class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp 完全背包问题 本题不强调是排列or组合
        # 如果求组合数就是外层for循环遍历物品，内层for遍历背包。
        # 如果求排列数就是外层for遍历背包，内层for循环遍历物品。
        res = -1
        # dp[j]：凑足总额为j所需钱币的最少个数为dp[j]
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
       
        # 遍历物品
        for coin in coins:
            # 遍历背包
            for j in range(coin, amount+1):   
                dp[j] = min(dp[j], dp[j-coin]+1)
            
        return dp[amount] if dp[amount] != float("inf") else -1
        
