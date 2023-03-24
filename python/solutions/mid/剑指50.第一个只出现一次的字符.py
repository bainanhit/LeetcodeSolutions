class Solution:
    # 有序字典
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return ' '
        n = len(s)
        dic = collections.OrderedDict()

        for c in s:
            dic[c] = not c in dic
        for k, v in dic.items():
            if v == True:
                return k

        return ' '