class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # 单调队列 + 滑动窗口
        # 2个单调队列维护当前滑动窗口的最大最小值  目的是为了避免重新遍历数组 来获取 某个范围内的 最大值和最小值
        n = len(nums)
        res = 0
        # 队首为当前最值
        q_min, q_max = collections.deque(), collections.deque()
        left, right = 0, 0
        while right < n:
            # 加入新元素，维护单调性
            # 队首对应left，队尾对应right
            while q_min and nums[q_min[0]] > nums[right]:
                q_min.popleft()
            q_min.appendleft(right)
            while q_max and nums[q_max[0]] < nums[right]:
                q_max.popleft()
            q_max.appendleft(right)
            
            while nums[q_max[-1]] - nums[q_min[-1]] > limit:
                left += 1
                if q_min and q_min[-1] < left:
                    q_min.pop()
                if q_max and q_max[-1] < left:
                    q_max.pop()

            res = max(res, right-left+1)
            right += 1

        return res

'''
maxQ 的 peek() 是 [left, right] 中的最大值
minQ 的 peek() 是 [left, right] 中的最小值

nums = [8,2,4,7], limit = 4
idx     0 1 2 3
首先插入 8 和 2
队列情况如下：
maxQ = {1, 0}   （peek() == 0）
minQ = {1}      （peek() == 1）

滑动窗口区间：[0, 1]

我们发现最大值和最小值的差 > 4，因此我们需要找到舍弃某些值，重新划定窗口区间
因为最大值的索引位置为 0，最小值的索引位置为 1，因此我们舍弃掉 0 位置 及前面的值，将 left 指向 0 后面的一个值，即 1
'''