class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 模拟
        # 时间复杂度为O(N)，空间复杂度为O(1)
        n = len(nums)
        k = 0
        i = n-2
        # 从右往左找第一个升序对
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        # 如果找到了
        if i >= 0:
            j = n-1
            # 从右往左找第一个比 nums[i] 大的元素
            while j>i and nums[j] <= nums[i]:
                j -= 1
            # 交换 nums[i] 与 nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # 反转右侧子数组
        l, r = i+1, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1





        
        


        

            

        