class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        path = []
        paths = []
        # 回溯
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


# fu: 字符串的全组合，要求结果中没有重复组合