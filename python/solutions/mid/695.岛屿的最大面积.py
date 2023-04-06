class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0
        def dfs(grid, i, j):
            nonlocal cnt
            if i >= m or i < 0 or j >= n or j < 0 or grid[i][j] != 1:
                return 0
            grid[i][j] = 2
            cnt += 1
            dfs(grid, i, j-1)
            dfs(grid, i, j+1)
            dfs(grid, i-1, j)
            dfs(grid, i+1, j)
            return cnt
        
        if m == 0 or n == 0:
            return 0
        res = 0
        for i in range(m):
            for j in range(n):
                # 访问每一个小岛, 清零cnt, 寻找最大值
                if grid[i][j] == 1:
                    cnt = dfs(grid, i, j)
                    res = max(res, cnt)
                    cnt = 0
        return res