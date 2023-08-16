class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp
        # dp[i]表示s的前i位能否用word dict中的单词表示
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = 1
        
        return True if dp[-1] == 1 else False