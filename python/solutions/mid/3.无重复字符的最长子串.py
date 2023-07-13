class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口
        # O(N) Z(N)
        if not s:
            return 0
        n = len(s)
        left = 0
        # 查找字典
        lookup = set()
        max_len = 0
        cur_len = 0 # 滑动窗口长度
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            max_len = max(max_len, cur_len)
            lookup.add(s[i])
        
        return max_len
    
# follow up: 至少k个重复的最长子串 lc395