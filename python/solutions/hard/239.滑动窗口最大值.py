import collections

class MyQueue:
    # 单调队列，从大到小
    def __init__(self):
        self.queue = collections.deque([])
        

    def front(self):
        # 查询当前队列最大值
        return self.queue[0]
    
    def pop_(self, val):
        if self.queue and self.queue[0] == val:
            self.queue.popleft()

    def push_(self, val):
        while self.queue and val > self.queue[-1]:
            self.queue.pop()
        self.queue.append(val)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        que = MyQueue()
        if not nums:
            return nums
        n = len(nums)

        for i in range(k):
            que.push_(nums[i])
        res.append(que.front())
        
        for i in range(k, n):
            # 滑动窗口加入、删除值
            que.pop_(nums[i - k])
            que.push_(nums[i])
            # 记录结果
            res.append(que.front())
        
        return res