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


# fu: lc213 打家劫舍2
class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp
        # 把环拆成两个队列，一个是从0到n-1，另一个是从1到n，然后返回两个结果最大的
        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]
        dp1 = [0] * n
        dp2 = [0] * n
        dp1[1] = nums[0] # 从第0个房屋开始偷
        dp2[1] = nums[1] # 从第1个房屋开始偷
        for i in range(2, n):
            dp1[i] = max(dp1[i-2]+nums[i-1], dp1[i-1])
            dp2[i] = max(dp2[i-2]+nums[i], dp2[i-1])
        
        res = max(dp1[-1], dp2[-1])
        return res