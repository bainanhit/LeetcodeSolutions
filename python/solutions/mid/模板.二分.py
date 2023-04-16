# 有序数组 二分查找
def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums)-1
    #  当left==right，区间[left, right]依然有效，所以用 <=
    while l <= r:
        mid = (r+l)//2
        if nums[mid] < target:
            l = mid+1
        elif nums[mid] > target:
            r = mid-1
        else:
            return mid
    
    return -1
            