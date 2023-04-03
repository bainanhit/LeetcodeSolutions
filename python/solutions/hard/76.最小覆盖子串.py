class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # ht统计t每个字符出现的次数,hs统计窗口中每个字符出现的次数,这里得用一个cnt来统计有效覆盖的数量,当cnt==t.size(),说明已经全覆盖了
        s_len = len(s)
        t_len = len(t)
        res = ''
        if not s or s_len <t_len:
            return ''
        if s == t:
            return s
        dic_t = collections.defaultdict(int)
        dic_s = collections.defaultdict(int)
        for c in t:
            dic_t[c] += 1
        dic_t_len = len(dic_t)
        l, r = 0, 0
        # cnt来统计有效覆盖的数量,当cnt==t.size(),说明已经全覆盖了
        cnt = 0
        while r < s_len:
            dic_s[s[r]] += 1
            # 如果加入后是小于等于ht中对应的字符,说明这个字符加入是不多余的,是有效的
            if dic_s[s[r]] <= dic_t[s[r]]:
                cnt += 1
            while l < s_len and dic_s[s[l]] > dic_t[s[l]]:
                dic_s[s[l]] -= 1
                l += 1
            # 如果有小覆盖数量为t.size那就更新答案
            if cnt == len(t):
                if not res or len(res) > r-l+1:
                    res = s[l: r+1] 
            r += 1

        return res