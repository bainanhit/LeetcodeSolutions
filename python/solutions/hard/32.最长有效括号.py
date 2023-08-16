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
                # 每次遇到一个右括号，则先把栈顶的元素弹出，如果弹出后当前栈变成空栈，则需要将当前右括号所在位置入栈，
                # 否则需要根据当前栈顶元素和当前右括号下标计算当前有效括号子串的长度，并更新结果变量res
                stack.pop()
                # 匹配左括号
                if not stack:
                    stack.append(i)
                else:
                    tmp_len = i-stack[-1]
                    max_len = max(max_len, tmp_len)
            
        return max_len

