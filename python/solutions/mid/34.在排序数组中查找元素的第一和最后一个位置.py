class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 二分
        n = len(nums)

        def rightBorder(nums, target):
            l, r = 0, len(nums)-1
            record = -1 # r边界下标
            # 当left==right，区间[left, right]依然有效
            while l <= r:
                mid = l + (r-l)//2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else: 
                    # 寻找右边界，nums[middle] == target的时候更新left
                    record = mid
                    l = mid + 1
            return record 
        
        def leftBorder(nums, target):
            l, r = 0, len(nums)-1
            record = -1 # r边界下标
            # 当left==right，区间[left, right]依然有效
            while l <= r:
                mid = l + (r-l)//2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else: 
                    record = mid
                    r = mid - 1 # 向左边压缩空间，继续查找
            return record

        lb = leftBorder(nums, target)
        rb = rightBorder(nums, target)
        
        return [lb, rb]
                
        