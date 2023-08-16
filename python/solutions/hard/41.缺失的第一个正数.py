class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 置换法
        # 思路：如果1 <= x <=n 那么x应该出现在第x-1的位置
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                # 使用while一直置换到发现不满足要求数字为止
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i in range(n):
            if nums[i] != i+1:
                return i+1
        
        return n+1
