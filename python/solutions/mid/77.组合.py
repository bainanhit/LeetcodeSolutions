class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 回溯
        path = []
        paths = []
        
        def backtrack(n, k, start):
            if len(path) == k:
                paths.append(path[:])
                return
            for i in range(start, n+1):
                path.append(i)
                backtrack(n, k, i+1)
                path.pop()
        
        backtrack(n, k, 1)
        return paths
