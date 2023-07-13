class Solution:
    # fu: 最多允许重复k次
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        def solve(k, nums):
            cnt = 0
            for i in range(0, n):
                if cnt < k or nums[cnt-k] != nums[i]:
                    nums[cnt] = nums[i]
                    cnt += 1
            return cnt
        
        return solve(2, nums)
