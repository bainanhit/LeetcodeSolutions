class Solution:
    # 复杂度O(n2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1
        # dp[i]表示i之前包括i的最长上升子序列的长度。
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        
        return res


# 优化
class Solution:
    # 贪心+二分:O(nlogn)
    def lengthOfLIS(self, nums: List[int]) -> int:
