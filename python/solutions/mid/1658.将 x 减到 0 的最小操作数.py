class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 滑动窗口法
        res = -1
        total = sum(nums)
        n = len(nums)
        l, r = 0, 0
        # 寻找一个最大滑动窗口 使得滑动窗口中的和为sum-x
        tar = total - x
        if total < x:
            return -1
        tmp = 0
        while r < n:
            tmp += nums[r]
            while l <= r and tmp > tar:
                tmp -= nums[l]
                l += 1
            if tar == tmp:
                res = max(res, r-l+1)
            r += 1

        return n-res if res>=0 else -1