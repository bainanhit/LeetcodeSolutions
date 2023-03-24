class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        res = False
        l, r = 0, len(nums)-1
        # 预处理: 将左右两边重复的元素 进行筛选。
        # 保证left和right和其前面的不相等，通过mid和right / left的比较，判断出哪边是有序的
        while l < r and nums[l] == nums[l+1]:
            l += 1
        while l < r and nums[r] == nums[r-1]:
            r -= 1

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            # 右边有序
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            # 左边有序
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            
        return res

        