class Solution:
    def calculate(self, s: str) -> int:
        # 功能为实现eval()
        sign = 1
        res = 0
        stack = []
        n = len(s)
        i = 0
        while i < n:
            if s[i].isdigit():
                curr = 0
                while i < n and s[i].isdigit():
                    curr = curr * 10 + int(s[i])
                    i += 1
                res += sign * curr
                continue
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append([res, sign])
                res, sign = 0, 1
            elif s[i] == ')':
                [last_res, last_sign] = stack.pop()
                res = last_res + last_sign * res
            # print(res)
            i += 1  
        return res

                
            