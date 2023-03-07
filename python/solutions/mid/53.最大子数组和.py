class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [nums[0]]
        res = nums[0]
        for i in range(1, n):
            tmp = max(nums[i], dp[i-1]+nums[i])
            dp.append(tmp)
            res = max(tmp, res)

        return res
            
