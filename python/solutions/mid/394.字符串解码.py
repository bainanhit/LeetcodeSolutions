class Solution:
    def decodeString(self, s: str) -> str:
        # 双栈  
        num_stack = []
        str_stack = []
        i, n = 0, len(s)
        num = 0
        res = ''
        while i < n:
            if s[i].isdigit():
                num = num*10 + int(s[i])
                i += 1
            elif s[i] == '[':
                # 将临时数字和临时字符串入栈
                num_stack.append(num)
                str_stack.append(res)
                # 初始化
                num = 0
                res = ''
                i += 1
            elif s[i] == ']':
                # 将数字和字符串出栈
                tmp_res = str_stack.pop()
                cnt = num_stack.pop()
                res = tmp_res + cnt*res
                i += 1
            else:
                res += s[i]
                i += 1
        return res
