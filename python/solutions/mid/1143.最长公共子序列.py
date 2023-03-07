class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp
        len1 = len(text1)
        len2 = len(text2)
        # dp[i,j]代表text1[0, i-1]与text2[0, j-1]公共子序列最长长度
        dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
    
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        
        return dp[-1][-1]