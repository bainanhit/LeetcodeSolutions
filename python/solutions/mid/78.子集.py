class Solution:
    # 回溯
    def __init__(self):
        self.path = []
        self.paths = []

    def backtrack(self, nums, start_index):
        # 收集子集，先于判断终止
        self.paths.append(self.path[:])
        # 返回条件
        if start_index == len(nums):
            return
        # 单层递归逻辑
        for i in range(start_index, len(nums)):
            self.path.append(nums[i])
            self.backtrack(nums, i+1)
            self.path.pop() # 回溯

    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.backtrack(nums, 0)
        return self.paths