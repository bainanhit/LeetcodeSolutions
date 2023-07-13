class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # DP
        # dp[i][j] 表示以下标i-1为结尾的字符串word1，和以下标j-1为结尾的字符串word2，最近编辑距离为dp[i][j]
        # 操作：1.word1删除1个元素 2.word2删除1个元素 3.word1修改元素
        m, n = len(word1)+1, len(word2)+1
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(m):
            dp[i][0] = i
        for j in range(n):
            dp[0][j] = j
        # 下标从1开始
        for i in range(1, m):
            for j in range(1, n):
                # 不变
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 替换，word1删除（相当于word2增加），word2删除
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        return dp[-1][-1]