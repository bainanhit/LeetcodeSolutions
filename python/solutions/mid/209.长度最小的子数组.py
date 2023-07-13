class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 滑动窗口
        # O(n) Z(1)
        n = len(nums)
        res = n+1
        cur_sum = 0
        start, end = 0, 0
        while end < n:
            cur_sum += nums[end]
            while cur_sum >= target:
                res = min(res, end-start+1)
                cur_sum -= nums[start]
                start += 1
            end += 1
        return 0 if res == n+1 else res
                
        