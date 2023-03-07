class Solution:
    def myAtoi(self, s: str) -> int:
        # 面向测试用例编程
        n = len(s)
        flag = 1
        cnt = 0
        res, nres = 0, 0
        if not s:
            return 0
        # 先判断cnt<n，否则s[cnt]会报错
        while cnt < n and s[cnt]==' ':
            cnt += 1
        if cnt == n:
            return 0
        if s[cnt] == '-':
            flag = 0
            cnt += 1
        elif s[cnt] == '+':
            cnt += 1
        
        while cnt < n and s[cnt] == '0':
            cnt += 1

        idx_cnt = 0
        while cnt < n and s[cnt].isdigit() and idx_cnt < 12:
            if not s[cnt].isdigit():
                break
            res = 10*res + int(s[cnt])
            cnt += 1
            idx_cnt += 1
        
        inf, ninf = (1<<31)-1, -(1<<31)
        if flag == 0 and -res <= ninf:
            return ninf
        if flag == 1 and res >= inf:
            return inf
        
        return res if flag else -res
        