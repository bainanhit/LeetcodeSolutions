from heapq import *

class MedianFinder:
    #大顶堆+小顶堆
    # O(logN) Z(N)
    def __init__(self):
        self.a = [] # 小顶堆，保存较大的一半
        self.b = [] # 大顶堆，保存较小的一半

    def addNum(self, num: int) -> None:
        if len(self.a) != len(self.b):
            heappush(self.a, num)
            heappush(self.b, -heappop(self.a))
        else:
            heappush(self.b, -num)
            heappush(self.a, -heappop(self.b))

    def findMedian(self) -> float:
        return self.a[0] if len(self.a) != len(self.b) else (self.a[0]-self.b[0])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()