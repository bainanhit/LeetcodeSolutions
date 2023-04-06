class KthLargest:
    # 最小堆
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.nums = nums
        self.k = k
        while len(self.nums) > self.k:
            # pop掉堆顶元素（最小的）
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        else:
            # 维护前k大的堆
            heapq.heappushpop(self.nums, val)

        # print(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)