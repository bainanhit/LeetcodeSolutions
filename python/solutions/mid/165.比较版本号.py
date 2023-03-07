class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # 双指针
        cnt = 0
        res = 0
        m, n = len(version1), len(version2)
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            x, y = 0, 0
            while p1 < m and version1[p1] != '.':
                x = x*10 + ord(version1[p1]) - ord('0')
                p1 += 1
            p1 += 1 # 跳过.号
            while p2 < n and version2[p2] != '.':
                y = y*10 + ord(version2[p2]) - ord('0')
                p2 += 1
            p2 += 1 # 跳过.号
            if x != y:
                return 1 if x > y else -1
        return 0
 