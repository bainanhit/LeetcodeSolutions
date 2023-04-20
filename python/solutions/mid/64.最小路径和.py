
class Solution:
    # 法一
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for j in range(1, n):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[-1][-1]
    
    # 滚动数组
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 初始化
        dp = grid[0]
        # 第0行
        for i in range(1, n):
            dp[i] += dp[i-1]
        
        for i in range(1, m):
            # 注意这里
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        
        return dp[-1]


    
    # 法二+输出具体路径：
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[0][1] = 0
        dp[1][0] = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i-1][j-1]

        return dp[m][n]
    
    # fu: 输出具体路径
    def generatePath(self, grid, dp):
         # 从终点处出发，反向寻找路径。
        i, j = len(dp) - 1, len(dp[0]) - 1
        res = [grid[i - 1][j - 1]]

        # 注意终止条件。
        while not (i == 1 and j == 1):
            if dp[i - 1][j] < dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
            res.append(grid[i - 1][j - 1])
