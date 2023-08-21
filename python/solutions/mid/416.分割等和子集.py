class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        target = target // 2
        # dp[i]中的i表示背包内总和
        dp = [0] * 10001
        # 0-1背包
        for num in nums:
            # 每一个元素一定是不可重复放入，所以从大到小遍历
            for j in range(target, num-1, -1):
                dp[j] = max(dp[j], dp[j-num]+num)
        
        # 集合中的元素正好可以凑成总和target
        if dp[target] == target:
            return True
        
        return False
