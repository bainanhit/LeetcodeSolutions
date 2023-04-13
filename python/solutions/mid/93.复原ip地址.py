class Solution:
    def __init__(self):
        self.res = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n < 4 or n > 12:
            return []
        self.backtrack(s, 0, 0)
        return self.res
        
        
    def isValid(self, s, start, end):
        if start > end:
            return False
        if s[start] == '0' and start != end:
            return False
        if not 0 <= int(s[start: end+1]) <= 255:
            return False
        
        return True

    def backtrack(self, s, start, point_num):
        if point_num == 3:
            if self.isValid(s, start, len(s)-1):
                self.res.append(s[:])
        for i in range(start, len(s)):
            # [start_index, i]就是被截取的子串
            if self.isValid(s, start, i):
                s = s[: i+1] + '.' + s[i+1:]
                self.backtrack(s, i+2, point_num+1)
                s = s[: i+1] + s[i+2:]
            else:
                break
        return None

