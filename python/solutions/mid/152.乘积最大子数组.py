class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp，此题使用两个变量来维护数组
        n = len(nums)
        if n == 1:
            return nums[0]
        res = 0
        # 一个保存最大的，一个保存最小的
        imax, imin = 0, 999999
        
        for i in range(n):
            # 如果数组的数是负数，那么会导致最大的变最小的，最小的变最大的。因此交换两个的值
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(imax*nums[i], nums[i])
            imin = min(imin*nums[i], nums[i])

            res = max(res, imax)
        
        return res
        