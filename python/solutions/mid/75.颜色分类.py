class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针
        n = len(nums)
        p0, p2 = 0, n-1
        cnt = 0

        while cnt <= p2:
            while cnt <= p2 and nums[cnt] == 2:
                nums[cnt], nums[p2] = nums[p2], nums[cnt]
                p2 -= 1
            if nums[cnt] == 0:
                nums[cnt], nums[p0] = nums[p0], nums[cnt]
                p0 += 1
            cnt += 1

            
                