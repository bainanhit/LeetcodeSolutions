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



# fu: 组合总和2 有重复元素  要求组合结果去重
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 先排序，再去重
        path = []
        paths = []
        candidates.sort(reverse=False)
        
        def backtrack(candidates, tmp_sum, start, target):
            if tmp_sum == target:
                paths.append(path[:])
                return 
            if tmp_sum > target:
                return
            
            for i in range(start, len(candidates)):
                # 去重
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                path.append(candidates[i])
                tmp_sum += candidates[i]
                backtrack(candidates, tmp_sum, i+1, target) # 每个数字只能用一次
                tmp_sum -= candidates[i]
                path.pop()
        
        backtrack(candidates, 0, 0, target)
        return paths

