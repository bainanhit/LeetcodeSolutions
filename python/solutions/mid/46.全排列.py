class Solution:
    def __init__(self):
        self.path = []
        self.paths = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [0] * n
        self.backtrack(nums, used)

        return self.paths

    def backtrack(self, nums, used):
        # 排列需要用Used标记
        if len(self.path) == len(nums):
            self.paths.append(self.path[:])
            return

        for i in range(len(nums)):
            if used[i] == 1:
                continue
            used[i] = 1
            self.path.append(nums[i])
            self.backtrack(nums, used)
            self.path.pop()
            used[i] = 0


# fu: 47.全排列2 去重
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        path = []
        paths = []
        nums.sort(reverse=False)
        used = [0] * (len(nums))
        
        def backtrack(nums, used):
            if len(path) == len(nums):
                paths.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and used[i-1]:
                    continue

                used[i] = 1
                path.append(nums[i])
                backtrack(nums, used)
                path.pop()
                used[i] = 0
        
        backtrack(nums, used)
        return paths
                 