class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        # 单调栈，存储下标
        stack = [0]
        for i in range(1, n):
            # 小于+等于
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    res[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        
        return res