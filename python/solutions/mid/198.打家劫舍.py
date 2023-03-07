class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp
        n = len(nums)
        # bad case
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # dp[i]代表第i个房子进入后能偷到的最高金额
        dp = [0] * (n)
        # 初始化
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        
        return dp[-1]