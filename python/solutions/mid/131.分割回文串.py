class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        path = []
        res = []
        if n == 1:
            res.append([s[0]])
            return res
        
        def isPalindrome(s):
            i, j = 0, len(s)-1
            while i < j:
                if s[i] != s[j]:
                    return 0
                i += 1
                j -= 1
            return 1
            
        
        def backtrack(start):
            if start == n:
                res.append(path[:])
                return
            for end in range(start, n):
                if isPalindrome(s[start: end+1]):
                    path.append(s[start: end+1])
                    backtrack(end+1)
                    path.pop()
        
            return None

        backtrack(0)
        return res
