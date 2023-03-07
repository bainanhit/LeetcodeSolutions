class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        # 多重背包 dp
        mod = 1e9 + 7
        # dp[i][j]前i题获得j分数的方法个数
        dp = [[0]*(target+1) for _ in range(len(types)+1)]
        dp[0][0] = 1
        # 第几题
        for i in range(1, len(types)+1):
            tmp = types[i-1][1] # 第i题分数
            for j in range(target+1): # 0-target分
            # 以上为0-1背包
                for k in range(types[i-1][0]+1): # 同分值题目数
                    if j - tmp*k >= 0:
                        # 表示第i题作对k个时，可能的次数；依次累加
                        dp[i][j] += dp[i-1][j-k*tmp]
                        dp[i][j] %= mod
        
        return int(dp[i][j])
                        
                        
        
