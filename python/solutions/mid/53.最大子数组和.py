class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] 表示：以 nums[i] 结尾的连续子数组的最大和
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
            

    # fu: 打印最大和的子数组
    def maxSubArray(self, nums: List[int]) -> List[int]:
        # dp[i] 表示：以 nums[i] 结尾的连续子数组的最大和
        n = len(nums)
        cur_sum, res = 0, float('-inf')
        l, tl, r = 0, 0, 0
        for i in range(n):
            cur_sum += nums[i]
            if cur_sum < nums[i]:
                cur_sum = nums[i]
                tl = i
            if cur_sum > res:
                res = cur_sum
                l = tl
                r = i
        
        return nums[l: r+1]