class Solution:
    # 复杂度O(n2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1
        # dp[i]表示i之前包括i的最长上升子序列的长度。
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        
        return res


    # fu：优化+输出路径
    # 贪心+二分:O(nlogn)
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lst = [nums[0]] # 存储路径
        for num in nums:
            if lst[-1] < num:
                # 当前元素大于列表尾部的元素，直接添加到列表尾部
                lst.append(num)
            else:
                # 当前元素不大于列表尾部的元素，使用二分法将其按照升序要求替换列表中已有的元素,列表中的总元素数不变
                l, r = 0, len(lst)-1
                while l < r:
                    mid = l +(r-l)//2
                    if num > lst[mid]:
                        l = mid+1
                    else:
                        r = mid
                # 替换
                lst[l] = num
        return len(lst)
        
