class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 二分 爬坡法
        # 当前比右边小，那么肯定在右边会有峰顶，最差情况走到头，也是一个峰顶； 如果当前比左边小，那么肯定在左边会有峰顶，最差情况一路走到头，也是一个峰顶。
        n = len(nums)
        l, r = 0, n-1
        res = 0
        def get(i):
            if i == -1 or i == n:
                return float('-inf')
            return nums[i]
        
        while l <= r:
            mid = (r+l) // 2
            if get(mid-1) < get(mid) > get(mid+1):
                res = mid
                break
            elif get(mid) < get(mid+1):
                l = mid + 1
            else:
                r = mid - 1
        
        return res

