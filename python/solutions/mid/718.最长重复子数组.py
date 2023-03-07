class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # dp or 滑动窗口, 本题采用dp
        
        m = len(nums1)
        n = len(nums2)
        dp = [0] * (n+1)
        res = 0
        
        for i in range(1, m+1):
            for j in range(n, 0, -1):
                # 注意从右向左遍历，否则会覆盖
                if nums1[i-1] == nums2[j-1]:
                    dp[j] = dp[j-1] + 1
                else:
                    dp[j] = 0
                res = max(res, dp[j])
                
        return res
        