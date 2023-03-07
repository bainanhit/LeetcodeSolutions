class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = 0
        left, right = 0, 0
        dp = [[0 for i in range(n)] for j in range(n)] 
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = 1
                    elif dp[i+1][j-1]:
                        dp[i][j] = 1
                if dp[i][j] and (j-i+1 > res):
                    res = j-i+1
                    left = i
                    right = j
        return s[left:right+1]

