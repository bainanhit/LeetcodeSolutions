class Solution:
    # DFS， 时间O(MN) 空间O(MN)
    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
            return
        # 一个岛所有的1都变成了2后，遍历的时候就不会重复遍历了
        grid[i][j] = '2'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    res += 1
        
        return res

    # Fu: BFS, 时间O(MN), 空间O(min(M, N))
    # def 