class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0]*(n+1) for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            nums = triangle[i]
            for j in range(len(nums)):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
                
        return dp[0][0]
    
    # 空间优化 滚动数组 一维dp
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0]*(n+1)
        for i in range(n-1, -1, -1):
            nums = triangle[i]
            for j in range(len(nums)):
                dp[j] = min(dp[j], dp[j+1]) + nums[j]

    # follow up: 输出路径
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0]*(n+1) for _ in range(n+1)]
        pre = [[0]*(n+1) for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            nums = triangle[i]
            for j in range(len(nums)):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
                if dp[i+1][j] < dp[i+1][j+1]:
                    pre[i+1][j] = 1
                else:
                    pre[i+1][j] = -1

        return dp[0][0]