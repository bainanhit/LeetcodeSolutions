class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 回溯
        if not board:
            return False
        m = len(board)
        n = len(board[0])
        length = len(word)
        visited = [[0 for _ in range(n)] for _ in range(m)]
        
        def backtrack(i, j, k):
            # 超出边界、已经访问过、已找到目标单词、棋盘格中当前字符已经和目标字符不一致了
            if board[i][j] != word[k] or i >= m or i < 0 or j >= n or j<0 or visited[i][j]:
                return False
            if k == length - 1:
                return True
            
            visited[i][j] = 1 # 修改当前节点状态
            # 回溯
            backtrack(i+1, j, k+1)
            backtrack(i-1, j, k+1)
            backtrack(i, j+1, k+1)
            backtrack(i, j-1, k+1)
            visited[i][j] = 0 # 撤销修改

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True

        return False