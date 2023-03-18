class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 双指针 dp
        # dp[i][j]：表示区间范围[i,j] （注意是左闭右闭）的子串是否是回文子串，如果是dp[i][j]为true，否则为false
        n = len(s)
        max_len = 0
        l, r = 0, 0
        dp = [[0] * n for _ in range(n)] 
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                # 转移方程
                if s[i] == s[j]:
                    if j-i <= 1:
                        dp[i][j] = 1
                    elif dp[i+1][j-1]:
                        dp[i][j] = 1
                # 更新下标记录
                if dp[i][j] and j-i+1 > max_len:
                    max_len = j-i+1
                    l, r = i, j
        
        return s[l:r+1]

