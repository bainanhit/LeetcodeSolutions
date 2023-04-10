class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # dp
        n = len(nums)
        count = [1] * n
        dp = [1] * n
        res = 0
        res_val = 0
        if n <= 1:
            return 1
        # count[i]记录了以nums[i]为结尾的字符串，最长递增子序列的个数
        # dp[i]记录了以nums[i]为结尾字符串 LIS的长度
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
                    dp[i] = max(dp[i], dp[j]+1)
                res = max(res, dp[i])

        for i in range(n):
            if res == dp[i]:
                res_val += count[i]
        
        return res_val