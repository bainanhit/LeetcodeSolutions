class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 栈里存储左括号的下标
        stack = [-1]
        tmp_len = 0
        max_len = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                # 匹配左括号
                if not stack:
                    stack.append(i)
                else:
                    tmp_len = i-stack[-1]
                    max_len = max(max_len, tmp_len)
            
        return max_len

