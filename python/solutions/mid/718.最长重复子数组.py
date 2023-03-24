class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # dp or 滑动窗口, 本题采用dp
        # 一维滚动数组
        m = len(nums1)
        n = len(nums2)
        dp = [0] * (n+1)
        res = 0
        
        for i in range(1, m+1):
            for j in range(n, 0, -1):
                # 注意从右向左遍历，否则会覆盖
                if nums1[i-1] == nums2[j-1]:
                    dp[j] = dp[j-1] + 1
                # 注意这里不相等的时候要有赋0的操作
                else:
                    dp[j] = 0
                    
                res = max(res, dp[j])
                
        return res
        