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