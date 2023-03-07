class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # T = O(2n) = O(n)
        n = len(nums)
        res = 10**6
        _sum = 0 # 滑动窗口内数值之和
        sub_len = 0 # 滑动窗口长度
        i = 0 # 滑动窗口起始位置
        for j in range(i, n):
            _sum += nums[j]
            # 注意这里使用while，每次更新 i（起始位置），并不断比较子序列是否符合条件
            while _sum >= target:
                sub_len = j - i + 1
                res = min(res, sub_len)
                _sum -= nums[i]
                i += 1
        # 如果result没有被赋值的话，就返回0，说明没有符合条件的子序列
        return res if res != 10**6 else 0
        