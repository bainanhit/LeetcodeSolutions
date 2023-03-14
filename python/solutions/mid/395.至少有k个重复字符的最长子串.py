class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # 分治
        if not s:
            return 0
        # 如果字符串中存在数量小于k的字符，那么该字符串必不合格，按照个数小于k的字符划分字符串，对划分的字符串继续递归判断
        for c in set(s):
            if s.count(c) < k:
                s = s.replace(c, '#')
            if '#' in s:
                return max(self.longestSubstring(t, k) for t in s.split('#'))

        return len(s) # 如果s中所有字符个数都大于k，返回s的长度