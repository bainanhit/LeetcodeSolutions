import collections

class MyQueue:
    # 单调队列，从大到小
    # O(N)
    def __init__(self):
        self.queue = collections.deque([])
        
    def front(self):
        # 查询当前队列最大值
        return self.queue[0]
    
    def pop_(self, val):
        # 每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出
        if self.queue and self.queue[0] == val:
            self.queue.popleft()

    def push_(self, val):
        # 如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止
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
        # 先将前k的元素放进队列
        for i in range(k):
            que.push_(nums[i])
        res.append(que.front())
        
        for i in range(k, n):
            que.pop_(nums[i - k]) #滑动窗口移除最前面元素
            que.push_(nums[i])  #滑动窗口前加入最后面的元素
            # 记录结果
            res.append(que.front())
        
        return res