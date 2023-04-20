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
    
    

# fu: 子集2 结果不能包含重复子集
def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        paths = []
        path = []
        nums.sort(reverse=False)

        def backtrack(nums, start):
            paths.append(path[:])
            if start == len(nums):
                return
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(nums, i+1)           
                path.pop()
        
        backtrack(nums, 0)
        return paths