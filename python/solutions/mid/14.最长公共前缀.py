class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 遍历
        res = ''
        n = len(strs)
        m = len(strs[0])
        cnt = 0
        if n <= 1:
            return strs[0]
        
        for i in range(m):
            for j in range(n):
                tmp_len = len(strs[j])
                if len(strs[j]) <= i or strs[0][i] != strs[j][i]:
                    return strs[0][:i]
        
        return strs[0]
            