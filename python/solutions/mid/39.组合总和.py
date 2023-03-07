class Solution:
    # 回溯
    def __init__(self):
        self.path = []
        self.paths = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        self.path.clear()
        self.paths.clear()
        self.backtrack(candidates, 0, target, 0)
        return self.paths

    
    def backtrack(self, candidates, sum_, target, start):
        # 边界条件
        if sum_ == target:
            self.paths.append(self.path[:])
            return
        if sum_ > target:
            return

        # 单层递归逻辑
        for i in range(start, len(candidates)):
            sum_ += candidates[i]
            # start += 1
            self.path.append(candidates[i])
            self.backtrack(candidates, sum_, target, i)
            # 回溯
            sum_ -= candidates[i]
            self.path.pop()
        
