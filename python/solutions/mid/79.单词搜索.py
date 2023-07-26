class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 回溯
        if not board:
            return False
        m, n = len(board), len(board[0])
        length = len(word)
        visited = [[0]*n for _ in range(m)]

        def backtrack(i, j, k):
            if i<0 or i>=m or j<0 or j>=n or visited[i][j] or board[i][j]!=word[k]:
                return False
            if length == k+1:
                return True
            visited[i][j] = 1
            res = backtrack(i+1, j, k+1) or backtrack(i, j+1, k+1) or backtrack(i-1, j, k+1) or backtrack(i, j-1, k+1) 

            visited[i][j] = 0
            return res
        
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        
        return False