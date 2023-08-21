class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        grid = ['.'*n for _ in range(n)]
        # print(grid)

        def isvalid(r, c):
            # 检查列
            for i in range(r):
                if grid[i][c] == 'Q':
                    return False
            
            # 检查45度  左上
            i, j = r-1, c-1
            while i >= 0 and j >=0:
                if grid[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            # 检查135度  右上
            i, j = r-1, c+1
            while i >= 0 and j <n:
                if grid[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            
            return True
        
        def backtrack(r):
            if r == n:
                # 棋盘填满，将当前解加入结果集
                res.append(grid[:])
                return 
            for c in range(n):
                if isvalid(r, c):
                    grid[r] = grid[r][:c] + 'Q' + grid[r][c+1:]
                    backtrack(r+1)
                    grid[r] = grid[r][:c] + '.' + grid[r][c+1:]
        
        backtrack(0)
        return res


            
                
            