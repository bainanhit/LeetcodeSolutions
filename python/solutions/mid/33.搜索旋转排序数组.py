class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        # 如果中间的数小于最右边的数，则右半段是有序的，若中间数大于最右边数，则左半段是有序的
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 右边有序
            elif nums[mid] < nums[right]:
                # target位于有序区间
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
            # 左边有序
            else:
                # target位于有序区间
                if nums[left] <= target and nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
        return -1