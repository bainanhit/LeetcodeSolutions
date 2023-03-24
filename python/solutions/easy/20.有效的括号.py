class Solution:
    def isValid(self, s: str) -> bool:
        char_stack = []
        n = len(s)
        left_chars_lst = ['(', '{', '[']
        right_chars_lst = [')', '}', ']']
        if not s:
            return True
        
        for item in s:
            if item == '(':
                char_stack.append(')')
            elif item == '[':
                char_stack.append(']')
            elif item == '{':
                char_stack.append('}')
            elif not char_stack or char_stack[-1] != item:
                return False
            else:
                char_stack.pop()
        
        return True if not char_stack else False